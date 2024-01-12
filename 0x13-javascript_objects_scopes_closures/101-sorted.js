#!/usr/bin/node
const object = require('./101-data').dict;
const newObject = {};

for (const key in object) {
  if (newObject[object[key]] !== undefined) {
    newObject[object[key]] = newObject[object[key]].concat(key);
  } else {
    newObject[object[key]] = [key];
  }
}
console.log(newObject);
