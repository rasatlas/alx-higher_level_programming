#!/usr/bin/node

/*
 * A script that prints a square.
 */

const myVar = parseInt(process.argv[2]);
let bucket = '';
if (!isNaN(myVar)) {
  for (let i = 0; i < myVar; i++) {
    for (let j = 0; j < myVar; j++) {
      bucket += 'X';
    }
    console.log(bucket);
    bucket = '';
  }
} else {
  console.log('Missing size');
}
