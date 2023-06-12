#!/usr/bin/node
function add( a, b) {
  const sum = a + b;
  console.log(sum);
}

const z = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

add(z, y);
