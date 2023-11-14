#!/usr/bin/node

/*
 * A script that prints the addition of 2 strings.
 */

function add (a, b) {
  const myVar1 = parseInt(a);
  const myVar2 = parseInt(b);
  return myVar1 + myVar2;
}

console.log(add(process.argv[2], process.argv[3]));
