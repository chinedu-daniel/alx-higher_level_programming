#!/usr/bin/node

const argumentsList = process.argv.slice(2);
const numbers = argumentsList.map(arg => parseInt(arg));

if (numbers.length < 2) {
  console.log(0);
} else {
  const sortedNumber = numbers.sort((a, b) => b - a);
  console.log(sortedNumber[1]);
}
