#!/usr/bin/node

const rq = require('request');
const url = process.argv[2];
let count = 0;

rq.get(url, (_, __, body) => {
  const results = JSON.parse(body).results;
  for (let i = 0; i < results.length; i++) {
    const result = results[i];
    const characters = result.characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].slice(-3) === '18/') {
        count++;
      }
    }
  }
  console.log(count);
});
