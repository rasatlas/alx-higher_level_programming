#!/usr/bin/node
/*
 * A class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * Create an instance method called print() that prints the rectangle
 * using the character X
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let bucket = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        bucket += 'X';
      }
      console.log(bucket);
      bucket = '';
    }
  }
}
module.exports = Rectangle;
