#!/usr/bin/node
/*
 * A function that returns the reversed version of a list.
 * You are not allowed to use the built-in method reverse.
 */

exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
