/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Destructuring in JavaScript
/// Date: May 26, 2026

/** Destructuring in JavaScript is a convenient way of extracting values 
 * from arrays or properties from objects into distinct variables. 
 * It allows for a more concise and readable syntax when working with complex 
 * data structures. Destructuring can be used with both arrays and objects,
 *  making it a versatile tool for handling data in JavaScript. **/

// Example of array destructuring
const numbers = [1, 2, 3, 4, 5];
const [first, second, ...rest] = numbers;

console.log(first); // Output: 1
console.log(second); // Output: 2
console.log(rest); // Output: [3, 4, 5]

console.log("-".repeat(20)); // Separator for clarity

// Example of object destructuring
const user = {
    name: "Alice",
    age: 30,
    city: "New York"
};

const { name, age } = user;

console.log(name); // Output: Alice
console.log(age); // Output: 30

console.log("-".repeat(20)); // Separator for clarity

// Example of undefined values in destructuring
const nums = [10, 20];
const [first, third] = nums;

console.log(first); // Output: 10
console.log(third); // Output: undefined

// Example of underfined  
const movie = {
    title: "Inception",
    year: 2010
};

const { title, director } = movie;

console.log(title); // Output: Inception
console.log(director); // Output: undefined

console.log("-".repeat(20)); // Separator for clarity
// Example of nested destructuring
const data = {
  numbers: [4, 7, 9],
  user: {
    name: "Vy"
  }
};

const [first, , third] = data.numbers;
const { name, age } = data.user;

console.log(first); // Output: 4
console.log(third); // Output: 9
console.log(name); // Output: Vy
console.log(age); // Output: undefined