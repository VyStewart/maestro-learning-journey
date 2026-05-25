/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: While loops in JavaScript
/// Date: May 25, 2026

/**  A while loop in JavaScript is a control flow statement that allows code to be 
 * executed repeatedly based on a given condition. The loop continues to execute 
 * as long as the specified condition evaluates to true. **/

// Example of a while loop
let count = 0;

while (count < 5) {
    console.log(count); // Output: 0, 1, 2, 3, 4
    count += 1; // Increment the count to avoid an infinite loop    
}

console.log("-".repeat(20)); // Separator for clarity   

// Example of a while loop
let number = 10;

while (number > 5) 
    {
        console.log(number); // Output: 10, 9, 8, 7, 6
        number -= 1; // Increment the number
    }

console.log("-".repeat(20)); // Separator for clarity

// Example of a while loop with a break statement
let i = 20;

while (i > 0) {
    console.log(i);
    if (i === 15) {
        break; // Exit the loop when i is 15
    }
    i -= 1; // Decrement i
}