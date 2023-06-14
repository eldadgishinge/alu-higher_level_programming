#!/usr/bin/node
import list from 100-data.js
let i = 0;
let nelist = list.map((item,index) => item * index);
console.log(nelist);
