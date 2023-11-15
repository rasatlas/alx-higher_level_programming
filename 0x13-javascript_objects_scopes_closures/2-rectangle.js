#!/usr/bin/node
/*
 * class Rectangle that define a rectangle.
 * The constructor must take 2 arguments w and h.
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not positive integer, create an empty object.
 */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || isNaN(w) || h <= 0 || isNaN(h)) {
      const Rectangle = {};
      return Rectangle;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
