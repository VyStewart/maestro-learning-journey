/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Spread Operator (...) in JavaScript
/// Date: May 26, 2026

/** The spread operator in JavaScript, denoted by three dots (...), 
 * is a powerful syntax that allows an iterable such as an array 
 * or an object to be expanded in places where zero or more arguments 
 * (for function calls) or elements (for array literals) are expected. 
 * It is commonly used for copying arrays, merging arrays, and spreading 
 * elements in function calls. The spread operator provides a concise 
 * and efficient way to work with arrays and objects in JavaScript. 
 * Primitives like numbers and strings are immutable
 * Arrays and objects are mutable and behave by reference.
 **/

// Example of assigning an array to another variable (by reference)
const a = [1, 2, 3];
const b = a;      // just assigning

b.push(4);

console.log("a:", a);   // Output: a: [1, 2, 3, 4]
console.log("b:", b);   // Output: b: [1, 2, 3, 4] - both a and b point to the same array

// Example of using the spread operator with arrays
const nums = [ 2, 3, 19, 93 ];
const numsCopy = [ ...nums ];
numsCopy.push(18);

console.log(nums); // Output: [ 2, 3, 19, 93 ]
console.log(numsCopy); // Output: [ 2, 3, 19, 93, 18 ]

console.log("-".repeat(20)); // Separator for clarity

// Example of using the spread operator with objects
const car = {
    brand: "Acura",
    year: 2015,
    color: "Dark Silver"
};

const copyCar = {...car};
copyCar.color = "Black";

console.log("Car:", car);
console.log(" Another Car:", copyCar);
