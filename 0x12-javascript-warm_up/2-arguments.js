#!/usr/bin/node

/*
 * A script that prints a message depending on the number of arguments passsed.
 */

const { argv } = require('node:process');
if (argv.length <= 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length > 3) {
  console.log('Arguments found');
}
