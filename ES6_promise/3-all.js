import { uploadPhoto, createUser } from './utils';

async function handleProfileSignup() {
  try {
    // Execute promises concurrently
    const [photoResponse, userResponse] = await Promise.all([
      uploadPhoto(),
      createUser()
    ]);

    // Extract firstName and lastName from userResponse
    const { firstName, lastName } = userResponse.body;

    // Log firstName and lastName
    console.log(`${photoResponse.body} ${firstName} ${lastName}`);
  } catch (error) {
    // Log error message if any of the promises fail
    console.error("Signup system offline");
  }
}

export default handleProfileSignup;
