#!/usr/bin/node
/*
 * A function that converts a number form base 10 to another base-
 * passed as argument.
 * Prototype: exports.converter = function (base)
 * You are not allowed to import any file.
 * You are not allowed to declare any new variable (var, let, etc)
 */

exports.converter = function (base) {
  return (number) => {
    return number.toString(base);
  };
};
