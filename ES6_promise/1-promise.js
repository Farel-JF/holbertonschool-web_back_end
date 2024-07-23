export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      // Resolve the promise with a success object
      resolve({
        status: 200,
        body: 'Success'
      });
    } else {
      // Reject the promise with an error object
      reject(new Error('The fake API is not working currently'));
    }
  });
}
