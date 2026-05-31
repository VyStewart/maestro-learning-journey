/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 03: Going Async
/// Topic: map() and filter() methods in JavaScript
/// Date: May 30, 2026

/** The map() and filter() methods are powerful array methods in JavaScript that allow 
 * you to transform and filter arrays in a functional programming style. 
 * The map() method creates a new array by applying a provided function to each element 
 * of the original array. It takes a callback function as an argument, which is executed 
 * for each element in the array, and returns a new array containing the results. 
 * The filter() method, on the other hand, creates a new array with all elements that pass 
 * a test implemented by the provided function. It also takes a callback function as an 
 * argument, which is executed for each element in the array, and returns a new array 
 * containing only the elements that satisfy the condition specified in the callback function. 
 * Both map() and filter() are non-destructive methods, meaning they do not modify the original 
 * array but instead return new arrays based on the transformations or filtering applied. **/

// Example of using map() to create a new array of doubled numbers
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(num => num * 2);

console.log("Doubled numbers:", doubled); // Output: Doubled numbers: [2, 4, 6, 8, 10]
console.log("Numbers:", numbers);         // Output: Numbers: [1, 2, 3, 4, 5]

console.log("-".repeat(20)); // Separator for clarity

const numbers2 = [10, 15, 20, 25, 30];
const numbs = numbers2.map(num => {
    console.log("Current number:", num);
});
console.log(numbs); // Output: [undefined, undefined, undefined, undefined, undefined]

console.log("-".repeat(20)); // Separator for clarity
// Example of using map() to create a new array of numbers.
const nums = [1, 2, 3];

const result = nums.map(n => {
  console.log('mapping', n);
  return n * 10;
});

console.log('result:', result); // Output: result: [10, 20, 30]
console.log('original:', nums); // Output: original: [1, 2, 3]

// Example of using filter() to create a new array of even numbers
const mixedNumbers = [1, 2, 3, 4, 5, 6];

const evenNumbers = mixedNumbers.filter(num => num % 2 === 0);

console.log("Even numbers:", evenNumbers); // Output: Even numbers: [2, 4, 6]
console.log("Mixed numbers:", mixedNumbers); // Output: Mixed numbers: [1, 2, 3, 4, 5, 6]

console.log("-".repeat(20)); // Separator for clarity
// Example of using filter() to create a new array of strings that contain the letter 'a'
const words = ["apple", "banana", "cherry", "date", "fig"];

const wordsWithA = words.filter(word => word.includes('a'));

console.log("Words with 'a':", wordsWithA); // Output: Words with 'a': ["apple", "banana", "date"]
console.log("Words:", words); // Output: Words: ["apple", "banana", "cherry", "date", "fig"]    

//console.log("-".repeat(20)); // Separator for clarity
// Example of using map() and filter() together to create a new nested array of stdents 
// with their names and scores.

const students = [
  { name: 'Alex', score: 75 },
  { name: 'Bella', score: 92 },
  { name: 'Chris', score: 81 },
  { name: 'Dana', score: 60 }
];

const upperNames = students.map(student => student.name.toUpperCase());

const topStudents = students.filter(student => student.score >= 80);

console.log("Names with Uppercase:", upperNames);
// Output: Names with Uppercase: ["ALEX", "BELLA", "CHRIS", "DANA"]
console.log("students with top scores:", topStudents)
// Output: students with top scores: [{ name: 'Bella', score: 92 }, { name: 'Chris', score: 81 }]