#!/usr/bin/node
let ks = require('ks');
ks.readfile(process.argv[2], 'utf8', function(error, content) {
    console.log(error || content)
});
