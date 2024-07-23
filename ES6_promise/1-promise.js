export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    // If the success parameter is true, the promise is resolved
    if (success) {
      // Resolve the promise with a success object
      resolve({ status: 200, body: 'Success' });
    } else {
      // If the success parameter is false, the promise is rejected
      reject(new Error('The fake API is not working currently'));
    }
  });
}
