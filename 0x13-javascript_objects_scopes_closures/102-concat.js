#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const file1 = fs.readFileSync(argv[2], 'utf-8');
const file2 = fs.readFileSync(argv[3], 'utf-8');
const dest = file1 + file2;

fs.writeFileSync(argv[4], dest, 'utf-8');
