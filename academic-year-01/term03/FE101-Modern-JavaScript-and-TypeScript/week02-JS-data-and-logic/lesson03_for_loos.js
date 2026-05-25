/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Forloops in JavaScript
/// Date: May 25, 2026

/**  A for loop in JavaScript is a control flow statement that allows code to be executed 
 * repeatedly based on a given condition. It consists of three parts: 
 * initialization, condition, and increment/decrement. The loop continues to execute 
 * as long as the specified condition evaluates to true. **/

// Example of a for loop
for (let i = 0; i < 5; i++) {
    console.log(i); // Output: 0, 1, 2, 3, 4
}   

console.log("-".repeat(20)); // Separator for clarity

// Example of a for loop with in a list
const fruits = ["apple", "banana", "cherry"];

for (let fruit of fruits) {
    console.log(fruit); // Output: apple, banana, cherry
}

console.log("-".repeat(20)); // Separator for clarity
// use classic for loop to iterate over the list and print the index and the value
let score = [85, 90, 78, 70,95];

for (let i = 0; i < score.length; i++) {
    console.log(`Index: ${i}, Value: ${score[i]}`);
}

// use for ....of loop when you only need the value and not the index