#!/usr/bin/node

const argsCount = process.argv.slice(2);
if ( argsCount[0] !== undefined){
    console.log( argsCount);
    }
else{
    console.log('No argument');
    }
