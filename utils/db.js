import { MongoClient } from 'mongodb';

class DBClient {
  constructor() {
    this.host = 'localhost';
    this.port = '27017';
    this.alive = false;
    if (process.env.DB_HOST) this.host = process.env.DB_HOST;
    if (process.env.DB_PORT) this.port = process.env.DB_PORT;
    if (process.env.DB_DATABASE) this.db = process.env.DB_DATABASE;
    this.client = new MongoClient(`mongodb://${this.host}:${this.port}`, {
      useUnifiedTopology: true,
    });
    this.client.connect(() => {
      this.alive = true;
    });
  }

  isAlive() {
    return this.alive;
  }

  async nbUsers() {
    const db = this.client.db('files_manager');
    return db.collection('users').countDocuments();
  }

  async nbFiles() {
    const db = this.client.db('files_manager');
    return db.collection('files').countDocuments();
  }

  async insertUser(object) {
    const db = this.client.db('files_manager');
    return db.collection('users').insertOne(object);
  }

  async findUser(object) {
    const db = this.client.db('files_manager');
    return db.collection('users').countDocuments(object);
  }

  async getUser(object) {
    const db = this.client.db('files_manager');
    return db.collection('users').findOne(object);
  }

  async delUser(object) {
    const db = this.client.db('files_manager');
    return db.collection('users').deleteOne(object);
  }
}

const dbClient = new DBClient();
export default dbClient;
