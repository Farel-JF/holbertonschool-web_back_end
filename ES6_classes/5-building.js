export default class building {
  constructor(sqft) {
    if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') { throw new Error('Class extending Building must override evacuationWarningMessage'); }
    this.sqft = sqft;
  }
  get sqft() {return this._sqft};
  set sqft(sqft){return this._sqft = sqlf};
}
