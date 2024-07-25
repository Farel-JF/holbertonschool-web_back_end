import building from "./5-building";

export default class SkyHighBuilding extends building() {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }
    get floors() {return this._floors; }

    set floors(floors) {return this._floors = floors; }

    evacuationWarningMessage() { return `Evacuate slowly the ${this._floors} floors`; }
}
