const fs = require('fs').promises;

function countStudents(path) {
    return fs.readFile(path, 'utf8')
        .then((data) => {
            // Split the file content into rows
            const lines = data.trim().split('\n');

            if (lines.length <= 1) {
                throw new Error('Cannot load the database');
            }

            // Remove the header (first line) and filter out empty rows
            const students = lines.slice(1).filter(line => line.trim() !== '');

            console.log(`Number of students: ${students.length}`);

            const fields = {};

            // Parse each student row
            students.forEach(student => {
                const [firstname, lastname, age, field] = student.split(',');

                if (!fields[field]) {
                    fields[field] = [];
                }

                fields[field].push(firstname);
            });

            // Log the number of students in each field and their names
            for (const field in fields) {
                const studentList = fields[field];
                console.log(`Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`);
            }
        })
        .catch(() => {
            throw new Error('Cannot load the database');
        });
}

module.exports = countStudents;
