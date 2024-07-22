export default class HolbertonCourse {
  constructor (name, length, students) {
    this._name = name
    this._lengh = length
    this._students = students
  }

  get name() {
    return this._name;
  }
  set name(name) {
  if (typeof name !== 'string') {
    throw new TypeError('Name must be a string');
  }
  this._name = name;
  }

  get lengh() {
    return this.lengh;
  }
  set lengh(lengh) {
  if (typeof length !== 'number') {
    throw new TypeError('Lengh must be a number');
  }
  this.lengh = lengh;
  }

  get students() {
    return this.students;
  }
  set students(students) {
  if (!Array.isArray(students)) {
    throw new TypeError('Students must be an array');
  }
  this.students = students;
  }
}
