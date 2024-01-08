#!/usr/bin/node
const argv = process.argv;
const arg1 = parseInt(argv[2]);
function factorial(a) {
  if (a === 0 || a === 1) {
    return a;
  } else if (isNaN(a)) {
      return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(arg1));
