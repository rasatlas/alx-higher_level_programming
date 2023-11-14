#!/usr/bin/node

/*
 * A script that searches the second biggest integer in the list of arguments.
 */

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const myArr = process.argv.slice(2).map(Number);
  console.log(myArr.sort((a, b) => a - b)[myArr.length - 2]);
}
