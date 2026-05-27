/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Intro to Functions in JavaScript
/// Date: May 26, 2026

/** Functions in JavaScript are reusable blocks of code that perform a specific task. 
 * They allow you to encapsulate logic and execute it whenever needed, 
 * making your code more modular and easier to maintain. Functions can be defined using function declarations, function expressions, or arrow functions. 
 * They can take parameters, return values, and can be invoked to perform their tasks. 
 * Functions are fundamental building blocks in JavaScript and are essential for 
 * creating dynamic and interactive web applications. **/

// Example of a function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("Alice")); // Output: Hello, Alice!

console.log("-".repeat(20)); // Separator for clarity
// Example of a function with no parameters
function greet() {
  console.log("Good morning, Have a good day!");
}

greet(); // Output: Good morning, Have a good day!

console.log("-".repeat(20)); // Separator for clarity
// Example of a function with parameters and return value
function add(a, b) {
    return a + b;
}

console.log(add(5, 3)); // Output: 8

console.log("-".repeat(20)); // Separator for clarity
// Example of input in a function
function add(a, b) {
    return a + b;
}

let result = add(10, 15);
console.log(result); // Output: 25

console.log("-".repeat(20)); // Separator for clarity
// Example of a function that returns an object
function analyzeNumbers(a, b) {
    return {sum: a + b, difference: a - b };
}

let result = analyzeNumbers(11, 18);
console.log(result); // Output: { sum: 29, difference: -7 }
