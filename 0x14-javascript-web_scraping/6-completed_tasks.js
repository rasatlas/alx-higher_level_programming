#!/usr/bin/node
/**
 * Script that computes the number of tasks completed by user id.
 * - The first argument is the API URL:
 * https://jsonplaceholder.typicode.com/todos
 * - Only print users with completed task
 * - You must use the module request
 */

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const dictionary = {};

    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (dictionary[data[i].userId] === undefined) {
          dictionary[data[i].userId] = 1;
        } else {
          dictionary[data[i].userId]++;
        }
      }
    }
    console.log(dictionary);
  } else {
    console.log(response.statusCode);
  }
});
