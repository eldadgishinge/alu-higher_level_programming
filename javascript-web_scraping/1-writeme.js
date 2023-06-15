#!/usr/bin/node
const fs = require('fs')
fs.writeFile( process.argv[3], 'utf8', error =>{
    if (error) console.log(error);
});
