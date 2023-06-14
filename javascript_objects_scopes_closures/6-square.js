#!/usr/bin/node

module.exports = class Square extends Square {

    charPrint(c) {

        if (c === undefined ){
            for (let i = 0; i < this.size; i++) console.log('X'.repeat(this.size));

        }else{
            for (let i = 0; i < this.size; i++) console.log(c.repeat(this.size));

        }
}
}
