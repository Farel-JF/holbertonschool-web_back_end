NodeJS Basics
Description
This project is part of the Holberton School curriculum focused on the fundamentals of NodeJS. The main objectives include running JavaScript using NodeJS, creating HTTP servers, and handling files using NodeJS modules.

Learning Objectives
By completing this project, you will learn how to:

Run JavaScript using NodeJS.
Use NodeJS modules to interact with the system and perform tasks like reading files.
Handle command-line arguments and environment variables using process.
Create HTTP servers using both Node's native http module and the Express framework.
Utilize ES6 features with NodeJS by configuring Babel.
Speed up development with Nodemon.
Test your code using Jest and ESLint.
Requirements
All files are written in JavaScript and executed on Ubuntu 20.04 LTS using NodeJS (version 20.x.x).
A README.md file is included at the root of the project folder.
Code is written in ES6 and follows the JavaScript Standard Style.
Files are linted using ESLint and tested using Jest.
Provided Files
database.csv: CSV file containing student data used for various tasks.
package.json: Project dependencies and scripts configuration.
.eslintrc.js: ESLint configuration file.
babel.config.js: Babel configuration for ES6 support.
Tasks
0. Executing basic JavaScript with NodeJS
File: 0-console.js
Function: displayMessage(string) – prints the string argument to stdout.
1. Using Process stdin
File: 1-stdin.js
A program that reads user input from stdin and displays the name entered.
2. Reading a file synchronously
File: 2-read_file.js
Function: countStudents(path) – reads a CSV file synchronously and displays student count per field.
3. Reading a file asynchronously
File: 3-read_file_async.js
Function: countStudents(path) – reads a CSV file asynchronously and returns a Promise.
4. Creating a simple HTTP server
File: 4-http.js
Creates an HTTP server that listens on port 1245 and displays "Hello Holberton School!" for any route.
5. Creating a more complex HTTP server
File: 5-http.js
Adds routing to handle / and /students, displaying student data from the CSV file.
6. Creating an HTTP server using Express
File: 6-http_express.js
Uses Express to create an HTTP server, listening on port 1245, displaying "Hello Holberton School!".
7. Creating more complex routes with Express
File: 7-http_express.js
Expands the Express server with routing for / and /students, showing student lists from a CSV.
8. Organizing the server structure
Directory: full_server/
Controllers, routes, and utilities organized into separate modules.
Fully functional server with detailed student listing routes, powered by Express.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/<your-github>/holbertonschool-web_back_end.git
Navigate to the project directory:
bash
Copy code
cd Node_JS_basic
Install the required dependencies:
Copy code
npm install
Testing
Run the tests using:

arduino
Copy code
npm run test
Lint the project using:

arduino
Copy code
npm run lint
