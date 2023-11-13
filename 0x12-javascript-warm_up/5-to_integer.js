#!/usr/bin/node
/*
 * A script that prints 'My number : <first argument converted into integer>'
 * if the first argument can be converted into integer
 */

const myVar = parseInt(process.argv[2]);
if (!isNaN(myVar)) {
  console.log('My number: ' + myVar);
} else {
  console.log('Not a number');
}
