/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Function as Values in JavaScript
/// Date: May 28, 2026

/** In JavaScript, functions are first-class citizens, which means they can 
 * be treated like any other value. This allows you to assign functions to 
 * variables, pass them as arguments to other functions, and return them 
 * from functions. 
 * This feature is fundamental to JavaScript's flexibility and enables 
 * powerful programming patterns such as callbacks, higher-order functions, 
 * and functional programming. 
 * Functions can be stored in data structures, passed around as values, 
 * and invoked dynamically, making JavaScript a versatile language for 
 * a wide range of programming tasks. **/

// Example of assigning a function to a variable
const greet = function (name) {
    console.log("Hello " + name + "!");
};

greet("Josh")   // Output: Hello Josh!

console.log("-".repeat(20)); // Separator for clarity
// Example of passing a function as an argument

const sayBye = function(name) {
    console.log("Bye " + name + "!");
};

function runTwice(action) {
    action("Josh");
    action("Vivi");
}

runTwice(sayBye);;
// Output:
// Bye Josh!
// Bye Vivi!

console.log("-".repeat(20)); // Separator for clarity
// Example of returning a function from another function
function double(n) {
    return n * 2;
}
function square(n){
    return n * n;
}

function printResult(num, operation) {
  const result = operation(num);
  console.log("Result is:", result);
}

printResult(5, double);     // Output: Result is: 10
printResult(9, square);     // Output: Result is: 81