/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Arrow Functions in JavaScript
/// Date: May 28, 2026

/** Arrow functions, introduced in ES6, provide a concise syntax for writing
 * functions in JavaScript. They are often used for writing shorter function
 * expressions and for maintaining the lexical scope of the `this` keyword.
 * Arrow functions do not have their own `this` context; instead, they inherit
 * it from the surrounding code. This makes them particularly useful in
 * situations where you want to preserve the context of `this`, such as in
 * callbacks or methods. 
 * The syntax for arrow functions is more compact than traditional function
 * expressions, making them a popular choice for writing cleaner and more
 * readable code. **/

// Example of an arrow function assigned to a variable
const greet = (name) => {
    console.log("Hello " + name + "!");
};

greet("Josh")   // Output: Hello Josh!

console.log("-".repeat(20)); // Separator for clarity
// Example of an arrow function with implicit return
const sayHello = () => {
    console.log("Hello!");
};

const tripple = n => n * n * n;

const add = (a, b) => a + b;

sayHello();
console.log("Tripple is:", tripple(4));
console.log(`Total is: ${add(4, 6)}`);
// Output:
// Hello!
// Tripple is: 64
// Total is: 10

console.log("-".repeat(20)); // Separator for clarity
// Example of an arrow function with multiple statements
const logSum = (a, b) => {
  const sum = a + b;
  console.log("Sum is:", sum);
  return sum;
};
logSum(5, 7); // Output: Sum is: 12 
