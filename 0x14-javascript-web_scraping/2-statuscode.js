#!/usr/bin/node
/**
 * A script that display the status code of a GET request.
 * - The first argument is the URL to request(GET)
 * - The status code must be printed like code: <status code>
 * - You must use the module request
 */
const request = require('request');
const url = process.argv[2];

request(url, function (err, response) {
  if (err) throw err;
  console.log('code: ' + response.statusCode);
});
