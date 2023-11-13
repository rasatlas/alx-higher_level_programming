#!/usr/bin/node

/*
 * A script that prints a message depending on the number of arguments passsed.
 */

if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
}
