#!/usr/bin/node
const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  // Sort numbers in descending order
  const sorted = args.sort((a, b) => b - a);

  // Find the first number smaller than the largest (second biggest)
  const first = sorted[0];
  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] < first) {
      console.log(sorted[i]);
      process.exit(0);
    }
  }

  // If all numbers are equal, print the largest
  console.log(sorted[0]);
}
