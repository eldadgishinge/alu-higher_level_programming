#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
    }

    print(){
        this.width = w;
        this.height = h;
        for (let i = 0; i < w; i++){
            for (let i = 0; i< h; i++){
                console.log('X'.repeat(w,h))
            }

        }

    }
  };

