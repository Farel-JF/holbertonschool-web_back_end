import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const array1 = new ClassRoom(19);
  const array2 = new ClassRoom(20);
  const array3 = new ClassRoom(34);

  return [array1, array2, array3]
}
