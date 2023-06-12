#!/usr/bin/node
const prt = parseInt(process.argv[2]);



if (prt) {
  for (let i = 0; i < prt; i++) {
    console.log('X'.repeat(prt));
  }
} else {
  console.log('Missing size');
}

