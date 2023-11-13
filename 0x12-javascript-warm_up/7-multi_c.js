#!/usr/bin/node

/*
 * A script that prints x times "C is fun"
 */

const myVar = parseInt(process.argv[2]);
if (!isNaN(myVar)) {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
