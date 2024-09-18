const http = require('http');
const countStudents = require('./3-read_file_async');
const path = require('path');

const databaseFile = process.argv[2];

const app = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/plain');

    if (req.url === '/') {
        res.statusCode = 200;
        res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
        res.statusCode = 200;
        res.write('This is the list of our students\n');


        countStudents(databaseFile)
            .then(() => {
                res.end();
            })
            .catch((err) => {
                res.write(err.message);
                res.end();
            });
    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }
});


app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});


module.exports = app;
