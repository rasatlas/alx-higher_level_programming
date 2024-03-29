#!/usr/bin/node
/**
 * Script that prints the number of movies where the character
 * "Wedge Antilles" is present.
 * - The first argument is the API URL of the Star wars API:
 * (https://swapi-api.alx-tools.com/api/films/)
 * Wedge Antilles is character ID 18
 * - Your script must use this ID for filtering the result of the API
 * You must use the module request
 */

const request = require('request');
const url = process.argv[2];
const characterId = '18'; // Wedge Antilles' character ID

let count = 0;

request(url, (err, response, body) => {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const films = data.results;

    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        const link = films[i].characters[j];

        // Splitting the URL string by '/' and selecting the second-to-last element
        const parts = link.split('/');
        const id = parts[parts.length - 2];
        if (id === characterId) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(response.statusCode);
  }
});
