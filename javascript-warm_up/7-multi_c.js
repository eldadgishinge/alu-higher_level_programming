#!/usr/bin/node
const prt = parseInt(process.argv[2]);

if (prt) {
  for (let i = 0; i < prt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
