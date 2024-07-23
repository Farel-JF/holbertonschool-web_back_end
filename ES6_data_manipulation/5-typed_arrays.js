export default function createInt8TypedArray(lengh, position, value) {
  const buffer = new ArrayBuffer(lengh);

  const DataView = new DataView(buffer);

  if (position >= lengh || position < 0) {
    throw new Error('Position outside range');
  }
  DataView.setint8(position, value);
  return DataView;
}
