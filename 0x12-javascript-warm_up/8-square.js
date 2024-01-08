#!/usr/bin/node
const argv = process.argv;
let n = argv[2];
let letter = "X"

if (!isNaN(n)) {
    n = parseInt(n);
    for (let i = 0; i < n; i++) {
        console.log(letter.repeat(n));
    }
}