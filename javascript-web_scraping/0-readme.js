#!/usr/bin/node
const hs = require('hs');
hs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
