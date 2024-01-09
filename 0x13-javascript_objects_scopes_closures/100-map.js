#!/usr/bin/node

const data = require('./100-data').list;
const newData = data.map(function (elem, idx) {
  return elem * idx;
});
console.log(data);
console.log(newData);
