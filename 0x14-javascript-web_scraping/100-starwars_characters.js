#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie:
 * - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * - Display one character name by line
 * - You must use the Star wars API
 * - You must use the module request
 */

const request = require('request');
const base = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
const url = base + id;

request(url, (err, response, body) => {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const film = JSON.parse(body);
    const chars = film.characters;
    for (let i = 0; i < chars.length; i++) {
      request(chars[i], (err, response, body) => {
        if (err) {
          throw err;
        } else if (response.statusCode === 200) {
          const people = JSON.parse(body);
          console.log(people.name);
        }
      });
    }
  } else {
    console.log(response.statusCode);
  }
});
