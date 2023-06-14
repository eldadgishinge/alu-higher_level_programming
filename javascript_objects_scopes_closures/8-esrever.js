#!/usr/bin/node
exports.esrever = function (list){
let j = list.length - 1 ;
let lest2 = []
for(let i = j; i >= 0; i-- ) {
  lest2.push(list[i])
  }
console.log(lest2)
}

