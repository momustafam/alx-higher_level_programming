#!/usr/bin/node

const rq = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
rq.get(url, (_, __, body) => {
  console.log(JSON.parse(body).title);
});
