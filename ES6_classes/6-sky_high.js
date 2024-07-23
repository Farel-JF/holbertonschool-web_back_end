import building from "./5-building";

export default class SkyHighBuilding extends building() {
  constructor(sqft, floors) {
    super(sqft);
    if (typeof floors !== 'number') {throw new TypeError('Floors must be a number'); }
    this.floors = floors;
  }
    get sqft() {
      return this._sqft;
  }
    set sqft(sqft) {return this.sqft = sqft }

    get floors() {return this._floors; }

    set floors(floors) {return this._floors = floors; }

    evacuationWarningMessage() {
      return `Evacuate slowly the ${this._floors} floors`;
  }
}
