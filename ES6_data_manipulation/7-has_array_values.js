export default function hasValuesFromArray(set, array) {
  if (!Array.isArray){
  return array.every(element => set.has(element));
  }
}
