export default class HolbertonClass {
  Constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  valueOf() {return this._size; }

  toString() { return this._location  }
}