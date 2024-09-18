const express = require('express');
const fs = require('fs');
const path = require('path');

// Create an Express application
const app = express();

// Helper function to count students asynchronously
const countStudents = (databasePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(databasePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = {};
      let totalStudents = 0;

      for (const line of lines.slice(1)) { // Skip the header
        const [firstname, , , field] = line.split(',');

        if (field) {
          if (!students[field]) students[field] = [];
          students[field].push(firstname);
          totalStudents++;
        }
      }

      let result = `Number of students: ${totalStudents}\n`;
      for (const [field, names] of Object.entries(students)) {
        result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      resolve(result.trim());
    });
  });
};

// Route for "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route for "/students"
app.get('/students', (req, res) => {
  const database = process.argv[2];
  if (!database) {
    res.status(500).send('Database file not provided');
    return;
  }

  countStudents(database)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((error) => {
      res.status(500).send(error.message);
    });
});

// Listen on port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Export the app
module.exports = app;
