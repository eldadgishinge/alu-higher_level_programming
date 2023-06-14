#!/usr/bin/node
const list = require('./100-data.js').list;
let nelist = list.map((item,index) => item * index);
console.log(nelist);
