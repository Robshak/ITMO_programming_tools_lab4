// server.ts
import express from 'express';

const app = express();
const port = 3000;

app.use(express.json());

app.get('/add', (req: any, res: any) => {
    const { a, b } = req.query;
    const sum = parseInt(a as string) + parseInt(b as string);
    res.json({ result: sum });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
