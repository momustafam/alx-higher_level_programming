#!/usr/bin/node

const rq = require('request');
const fs = require('fs');

const url = process.argv[2];
const fpath = process.argv[3];

rq.get(url, (_, __, body) => {
  fs.writeFile(fpath, body, 'utf-8', (err) => {
    if (err) console.log(err);
  });
});
