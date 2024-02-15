#!/usr/bin/node
/**
 * Check the parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate() {
     // Swap the values of width and height using a temporary variable
	let temp = this.width;
	  this.width = this.height;
	  this.height = temp;
  }

 double () {
	 // multiples the width and the height of the rectangle by 2
	this.width *= 2;
	 this.height *= 2;
 }
  print () {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += 'X';
        y++;
      }

      console.log(myVar);
    }
  }
}
module.exports = Rectangle;
