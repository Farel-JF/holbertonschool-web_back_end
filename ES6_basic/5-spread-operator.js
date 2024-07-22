export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string]
}
console.log(concalArrays(['a', 'b'], ['c', 'd'], 'Hello'));
