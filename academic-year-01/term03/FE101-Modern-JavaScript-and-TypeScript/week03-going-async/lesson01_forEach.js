/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 03: Going Async
/// Topic: forEach() as first callback pattern in JavaScript
/// Date: May 30, 2026

/** The forEach() method is a built-in array method in JavaScript that allows you
 * to execute a provided function once for each array element. It is commonly
 * used for iterating over arrays and performing side effects, such as logging
 * values or modifying elements. The forEach() method takes a callback function
 * as an argument, which is executed for each element in the array. The callback
 * function can take up to three arguments: the current element, the index of the
 * current element, and the array being traversed. 
 * The forEach() method does not return a new array; instead, it returns
 * undefined. It is important to note that forEach() is not suitable for
 * asynchronous operations, as it does not wait for promises to resolve before
 * moving on to the next iteration. For asynchronous operations, other methods
 * like map(), filter(), or reduce() may be more appropriate. **/

// Example of using forEach() to log each element in an array
const colors = ["red", "green", "blue"];

colors.forEach(function(color, index){
    console.log(`Color at index ${index} is ${color}`);
});
// Output:
// Color at index 0 is red
// Color at index 1 is green
// Color at index 2 is blue

console.log("-".repeat(20)); // Separator for clarity
// Example of using forEach() to check if numbers are even or odd
const numbers = [9, 1, 2, 3, 4];

numbers.forEach((num, index) => {
    if (num % 2 === 0) {
        console.log(`${num} at index ${index} is even`) 
    } else {
        console.log(`${num} at index ${index} is odd.`)
    }
});