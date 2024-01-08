#!/usr/bin/node
const argv = process.argv;
const arg1 = parseInt(argv[2]);
function factorial(a) {
  if (isNaN(a) || a < 2) return 1;
  else return a * factorial(a - 1);
}
console.log(factorial(arg1));
