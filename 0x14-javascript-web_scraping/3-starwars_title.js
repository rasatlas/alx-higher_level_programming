#!/usr/bin/node
/**
 * A script that prints the title of a Star Wars movie where the
 * episode number matches a given integer
 * - The first argument is the movie ID
 * - You must use the Star Wars API (https://swapi-api.alx-tools.com/)
 * with the end point 'https://swapi-api.alx-tools.com/api/films/:id'
 * - You must use the module request
 */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
const endPoint = url + id;

request(endPoint, (err, response, body) => {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
      const data = JSON.parse(body);
      console.log(data.title);
  } else
      console.log(response.statusCode)
});
