#!/usr/bin/node
const prt = process.argv[2]

const z = Number(prt)

console.log(typeof(z))

if (Number){
    console.log('My number: ' + prt);
} else {
    console.log('Not a number');
}
