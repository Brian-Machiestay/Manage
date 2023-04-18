import crypto from 'crypto';
import { uuid } from 'uuidv4';
import dbClient from '../utils/db';
import redisClient from '../utils/redis';
/* global atob */

class AuthController {
  static async getConnect(req, res) {
    const auth = req.headers.authorization.split(' ')[1];
    const decryptDetails = atob(auth);
    if (decryptDetails.indexOf(':') === -1) {
      res.status(401).send({ error: 'Unauthorized' });
    } else {
      const details = decryptDetails.split(':');
      const email = details[0];
      const hash = crypto.createHash('sha1');
      const pass = hash.update(details[1]).digest('hex');
      if (await dbClient.findUser({ email, password: pass }) === 0) {
        res.status(401).send({ error: 'Unauthorized' });
      } else {
        const token = uuid();
        const thisUsr = await dbClient.getUser({ email, password: pass });
        const key = `auth_${token}`;
        await redisClient.set(key, thisUsr._id.toHexString(), 60 * 60 * 24);
        res.send({
          token,
        });
      }
    }
  }

  static async getDisconnect(req, res) {
    const token = req.headers['x-token'];
    const key = `auth_${token}`;
    const getUserId = await redisClient.get(key);
    if (getUserId === null) {
      res.status(401).send({
        error: 'Unauthorized',
      });
    } else {
      await redisClient.del(key);
      res.status(204).send();
    }
  }
}

export default AuthController;
