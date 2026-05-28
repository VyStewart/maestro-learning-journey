/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Anonymous Functions in JavaScript
/// Date: May 28, 2026

/** Anonymous functions, also known as function expressions, are functions
 * that do not have a name. They are often used in situations where a function
 * is needed temporarily, such as when passing a function as an argument to
 * another function or when defining a function inline. 
 * Anonymous functions can be defined using the function keyword or using
 * arrow function syntax. They are commonly used in callbacks, event handlers,
 * and immediately invoked function expressions (IIFEs). 
 * The flexibility of anonymous functions allows developers to write concise
 * and efficient code without the need for naming every function. **/

// Example of an anonymous function assigned to a variable
const greet = function (name) {
    console.log("Hello " + name + "!");
};

greet("Josh")   // Output: Hello Josh!

console.log("-".repeat(20)); // Separator for clarity

// Example of an anonymous function
console.log("First");

setTimeout(function() {
  console.log("Second");
}, 1000);

console.log("Third");

// Output:
// First
// Third
// Second (after 1 second delay)

console.log("-".repeat(20)); // Separator for clarity
// Example of an interval using an anonymous function
let counter = 0;

// we SAVE the "timer id" in intervalId
const intervalId = setInterval(function () {
  counter += 1;
  console.log("Tick");

  if (counter === 3) {
    clearInterval(intervalId); // use the same name here
  }
}, 500);
// Output:
// Tick (every 0.5 seconds, stops after 3 ticks)