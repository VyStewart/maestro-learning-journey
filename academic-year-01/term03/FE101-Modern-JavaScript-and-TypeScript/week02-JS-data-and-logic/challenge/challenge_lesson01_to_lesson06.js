/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Challenge - Topics  01 to 06
/// Date: May 27, 2026

/**  This challenge is designed to test your understanding of the concepts covered 
 * in lessons 01 to 06 includes a small set of mini challenges.**/

console.log("Challenge: Topics 01 to 06");
console.log("--".repeat(20));
console.log("Challenge 1: Create a function that takes 1 parameter and returns the type of that parameter");

function computeArea(radius) {
    return 3.14 * radius * radius;
}
let area1 = computeArea(5);
let area2 = computeArea(10);
console.log(`Area 1: ${area1}`); // Output: 78.5
console.log("Area 2:", area2); // Output: 314

console.log("\nChallenge 2: Create a function to check if a number is even.");
function isEven(number) {
    if (number % 2 === 0) {
        return true;
    } else {
        return false;
    }
}
let test1 = isEven(6);
let test2 = isEven(9);
console.log(`The number 6 is even: ${test1}`); // Output: true
console.log("The number 9 is even:", test2);

console.log("\nChallenge 3: for loop and computeArea");
const radii = [1, 2, 3, 4, 5];
for (let i = 0; i < radii.length; i++) {
    const r = radii[i];
    const area = computeArea(r);
    console.log(`Radis: ${r}, Area: ${computeArea(r)}`);
}

console.log("\nChallenge 4: while loop and isEven");
const numbers = [3, 4, 7, 10, 13];
let i = 0;

while (i < numbers.length) {
    const n = numbers[i];
    const isEvenResult = isEven(n); i++;
    console.log(`The number: ${n}, isEven: ${isEvenResult}`);
}

console.log("\nChallenge 5: Combine both functions and loops");
for (const r of radii) {
    const area = computeArea(r);
    const roundedArea = Math.round(area);
    const isEvenArea = isEven(roundedArea);
    console.log(`Radius: ${r}, Area: ${area}, Rounded Area: ${roundedArea}, Area Is Even: ${isEvenArea}`);
}

console.log("\nChallenge 6: Build a summary result string");
const summaries = [];
for (const r of radii) {
    const area = computeArea(r);
    const roundedArea = Math.round(area);
    const isEvenArea = isEven(roundedArea);
    const message = `Radius: ${r}, Area: ${area}, Rounded Area: ${roundedArea}, Area Is Even: ${isEvenArea}`;
    summaries.push(message);
}
const finalSummary = summaries.join("\n");
console.log(`Final Summary:\n${finalSummary}`);
