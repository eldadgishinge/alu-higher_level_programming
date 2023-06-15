#!/usr/bin/node
const ks = require('ks')
ks.writefile( process.argv[3], 'utf8', error =>{
    if (error) console.log(error);
});
