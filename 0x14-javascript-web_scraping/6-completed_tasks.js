#!/usr/bin/node

const rq = require('request');

const url = process.argv[2];
const nComp = {};
let completed;
let userId;

rq.get(url, (_, __, body) => {
  const todos = JSON.parse(body);
  for (let i = 0; i < todos.length; i++) {
    userId = todos[i].userId;
    completed = todos[i].completed;
    if (completed && userId in nComp) nComp[userId] += 1;
    else if (completed && !(userId in nComp)) nComp[userId] = 1;
  }
  console.log(nComp);
});
