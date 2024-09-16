const fs = require('fs');

function countStudents(path) {
    try {

        const data = fs.readFileSync(path, 'utf8');


        const lines = data.trim().split('\n');

        if (lines.length <= 1) {
            throw new Error('Cannot load the database');
        }


        const students = lines.slice(1).filter(line => line.trim() !== '');

        console.log(`Number of students: ${students.length}`);

        const fields = {};


        students.forEach(student => {
            const [firstname, lastname, age, field] = student.split(',');

            if (!fields[field]) {
                fields[field] = [];
            }

            fields[field].push(firstname);
        });

        
        for (const field in fields) {
            const studentList = fields[field];
            console.log(`Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`);
        }
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
