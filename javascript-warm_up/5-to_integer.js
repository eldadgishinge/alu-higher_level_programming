#!/usr/bin/node
const prt = parseInt(process.argv[2]);
if ( prt ){
  console.log('My number: ' + prt);
} else {
  console.log('Not a number');
}
