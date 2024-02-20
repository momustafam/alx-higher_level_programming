#!/usr/bin/node

const rq = require('request');
const url = process.argv[2];

rq.get(url, (_, resp) => {
  console.log('code: ' + resp.statusCode);
});
