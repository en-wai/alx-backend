// Import the Redis library using ES6 import syntax
import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Connect the client (asynchronous function)
(async () => {
  try {
    await client.connect();
  } catch (err) {
    console.error(`Redis client not connected to the server: ${err.message}`);
  }
})();
