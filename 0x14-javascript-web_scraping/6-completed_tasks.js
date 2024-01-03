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
let counter = 1;

request(url, (err, response, body) => {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);

    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        console.log(`'${counter}': ${data[i].id}`);
        counter++;
      }
    }
  } else {
    console.log(response.statusCode);
  }
});
