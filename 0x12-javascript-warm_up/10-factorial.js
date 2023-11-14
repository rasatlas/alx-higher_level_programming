#!/usr/bin/node

/*
 * A script that computes and prints a factorial
 */

function factorial (num) {
  const myVar = parseInt(num);
  if (isNaN(myVar) || myVar === 0 || myVar === 1) {
    return 1;
  } else {
    return myVar * factorial(myVar - 1);
  }
}

console.log(factorial(process.argv[2]));
