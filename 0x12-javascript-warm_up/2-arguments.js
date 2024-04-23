#!/usr/bin/node

const noArg = process.argv.slice(2);

if (noArg.length === 0) {
  console.log('No argument');
} else if (noArg.length === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
