/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Forloops in JavaScript
/// Date: May 25, 2026

/**  A for loop in JavaScript is a control flow statement that allows code to be executed 
 * repeatedly based on a given condition. It consists of three parts: 
 * initialization, condition, and increment/decrement. The loop continues to execute 
 * as long as the specified condition evaluates to true. **/

// Example of a for ..of loop (iterating over an array)
for (let i = 0; i < 5; i++) {
    console.log(i); // Output: 0, 1, 2, 3, 4
}   

console.log("-".repeat(20)); // Separator for clarity

// Example of a for ...of loop (iterating over an array and printing the value)
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

console.log("-".repeat(20)); // Separator for clarity
// example of a for ...in loop to iterate over the properties of an object
const person = {
    name: "John",
    age: 30,
    city: "New York"
};

for (let key in person) {
    console.log(`${key}: ${person[key]}`); // Output: name: John, age: 30, city: New York
}

// use for ....of loop when you only need the value and not the index

/* If you want to  indexes with an array in a for..of loop, use the entries() method */
const nums = [10, 20, 30];
for (const [index, value] of nums.entries()) {
  console.log(`Index: ${index}, Value: ${value}`);
}
// Output: Index: 0, Value: 10
//         Index: 1, Value: 20
//         Index: 2, Value: 30