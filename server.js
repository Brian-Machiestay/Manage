import app from './routes/index';

let port = 5000;
if (process.env.PORT) port = process.env.PORT;
app.listen(port, () => console.log(`this server is running on port ${port}`));
