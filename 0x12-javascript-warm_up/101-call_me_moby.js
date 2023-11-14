#!/usr/bin/node
/*
 * A function that executes x times a function.
 */

const callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

module.exports.callMeMoby = callMeMoby;
