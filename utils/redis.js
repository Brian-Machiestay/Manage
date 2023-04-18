import { createClient } from 'redis';

// A redis instance class for managing storage

class RedisClient {
  constructor() {
    this.client = createClient();
    this.alive = false;
    this.client.on('connect', () => {
      this.alive = true;
    });
    this.client.on('error', (err) => console.log(err));
  }

  isAlive() {
    return this.alive;
  }

  async get(key) {
    const val = new Promise((resolve, reject) => {
      this.client.get(key, (err, val) => {
        if (err) reject(err);
        else resolve(val);
      });
    });
    const actualVal = await val;
    return actualVal;
  }

  async set(key, value, due) {
    let val = new Promise((resolve, reject) => {
      this.client.set(key, value, (err, val) => {
        if (err) reject(err);
        else resolve(val);
      });
    });
    val = await val;
    await this.client.expire(key, due);
    return val;
  }

  async del(key) {
    await this.client.del(key);
  }
}

const redisClient = new RedisClient();
export default redisClient;
