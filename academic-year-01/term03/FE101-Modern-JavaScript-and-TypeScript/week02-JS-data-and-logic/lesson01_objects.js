/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Objects in JavaScript
/// Date: May 23, 2026

/**  Objects in JavaScript are collections of key-value pairs. They are used
 to store and organize data in a structured way. Each key is a string (or symbol) 
 that serves as an identifier for a value, which can be of any data type, 
 including other objects. Objects are fundamental to JavaScript and are used 
 in various ways, such as representing real-world entities, organizing data, 
 and creating complex data structures. **/

//Example of creating an object
const user = {
    name: "Alice",
    age: 30,
 };
 
// Assigning key as a variable
const key = "name";

// Accessing object properties using a variable key
console.log(user[key]); // Output: Alice

// Accessing object properties
console.log(user.name); // Output: Alice
console.log(user.age);  // Output: 30

// Accessing properties using bracket notation
console.log(user["name"]); // Output: Alice
console.log(user["age"]);  // Output: 30