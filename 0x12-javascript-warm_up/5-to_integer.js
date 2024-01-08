#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Not a Number');
} else {
  console.log(`My number: ${num}`);
}
