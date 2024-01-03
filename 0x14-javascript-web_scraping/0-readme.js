#!/usr/bin/node
/*
 * A script that reads and prints the content of a file.
 * - The file argument is the file path
 * - The content of the file must be read in utf-8
 * - If an error occurred during the reading, print the error object
 */

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
