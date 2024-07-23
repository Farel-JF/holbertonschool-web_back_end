export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);

  const View = new DataView(buffer);

  if (position >= lengh || position < 0) {
    throw new Error('Position outside range');
  }

  View.setInt8(position, value);

  return View;
}
