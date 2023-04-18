import express from 'express';
import AppController from '../controllers/AppController';
import UsersController from '../controllers/UsersController';
import AuthController from '../controllers/AuthController';

const app = express();
app.use(sessions({
    secret: 'mysecretkey',
    saveUninitialized: true,
    cookie: { maxAge: 60 * 60 * 24 },
    resave: false
}))

app.use(express.json());

app.get('/status', (req, res) => {
  AppController.getStatus(req, res);
});

app.get('/stats', (req, res) => {
  AppController.getStats(req, res);
});

app.post('/users', (req, res) => {
  UsersController.postNew(req, res);
});

app.get('/connect', (req, res) => {
  AuthController.getConnect(req, res);
});

app.get('/disconnect', (req, res) => {
  AuthController.getDisconnect(req, res);
});

app.get('/users/me', (req, res) => {
  UsersController.getMe(req, res);
});

export default app;
