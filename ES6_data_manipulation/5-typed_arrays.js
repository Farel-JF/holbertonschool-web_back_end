export default function createInt8TypedArray(length, position, value) {
  // Check if the position is out of the allowed range
  if (position >= length) {
    throw Error('Position outside range');
  }
  // Create a new ArrayBuffer with the specified size
  const buffer = new ArrayBuffer(length);
  // Create a DataView to manipulate the data in the ArrayBuffer
  const dataView = new DataView(buffer);
  // Set the value at the specified position
  dataView.setInt8(position, value);
  return dataView;
}
