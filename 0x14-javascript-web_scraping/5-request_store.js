#!/usr/bin/node
/**
 * Script that gets the contents of a webpage and stores it in a file.
 * - The first argument is the URL to request
 * - The second argument the file path to store the body response
 * - The file must be UTF-8 encoded
 * - You must use the module request
 */

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, 'utf8', (err, response, body) => {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const data = body;
    fs.writeFile(filePath, data, function (err) {
      if (err) throw err;
    });
  } else {
    console.log(response.statusCode);
  }
});
