import crypto from 'crypto';
import { ObjectId } from 'mongodb';
import dbClient from '../utils/db';
import redisClient from '../utils/redis';

class UsersController {
  static async postNew(req, res) {
    if (!req.body.email) {
      res.status(400).send(
        { error: 'Missing email' },
      );
    } else if (!req.body.password) res.status(400).send({ error: 'Missing password' });
    else if (await dbClient.findUser({ email: req.body.email }) > 0) {
      res.status(400).send({ error: 'Already exist' });
    } else {
      const hash = crypto.createHash('sha1');
      const ob = {
        email: req.body.email,
        password: hash.update(req.body.password).digest('hex'),
      };
      const { ops } = await dbClient.insertUser(ob);
      res.status(201).send({
        id: ops[0]._id,
        email: req.body.email,
      });
    }
  }

  static async getMe(req, res) {
    const token = req.headers['x-token'];
    const key = `auth_${token}`;
    const getUserId = await redisClient.get(key);
    const dbid = new ObjectId(getUserId);
    if (getUserId === null) {
      res.status(401).send({
        error: 'Unauthorized',
      });
    } else {
      const val = await dbClient.getUser({ _id: dbid });
      res.send({
        id: val._id,
        email: val.email,
      });
    }
  }
}

export default UsersController;
