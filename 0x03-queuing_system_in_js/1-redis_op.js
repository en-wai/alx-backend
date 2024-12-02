// Import the Redis library using ES6 import syntax
import { createClient } from 'redis';
// Import 'print' for confirmation messages
import { print } from 'redis/lib/utils'; 
// Create a Redis client
const client = createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
   // Call the functions after the client is connected
  displaySchoolValue('Holberton'); // Retrieve the value for 'Holberton' (initially may not exist)
  setNewSchool('HolbertonSanFrancisco', '100'); // Set a new key-value pair
  displaySchoolValue('HolbertonSanFrancisco'); // Retrieve the value for 'HolbertonSanFrancisco'
  
});

// Handle connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Function to set a new key-value pair in Redis.
 * @param {string} schoolName - The key to set in Redis.
 * @param {string} value - The value to set for the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // 'print' displays the result of the operation
}

/**
 * Function to retrieve and display the value of a key from Redis.
 * @param {string} schoolName - The key to retrieve from Redis.
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
    } else {
      console.log(value); // Log the retrieved value
    }
  });
}


// Connect the client (asynchronous function)
(async () => {
  try {
    await client.connect();
  } catch (err) {
    console.error(`Redis client not connected to the server: ${err.message}`);
  }
})();


