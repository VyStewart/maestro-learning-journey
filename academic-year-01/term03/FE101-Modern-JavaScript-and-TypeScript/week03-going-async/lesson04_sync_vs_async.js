/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 03: Going Async
/// Topic: Synchronous vs Asynchronous JavaScript
/// Date: June 01, 2026

/** Synchronous JavaScript executes code in a sequential manner, meaning that each line of code 
 * is executed one after the other. In synchronous code, if a particular operation takes a long 
 * time to complete, it will block the  execution of the subsequent code until it finishes.
 * This can lead to a poor user experience, especially if the operation involves network 
 * requests or heavy computations.
 * Asynchronous JavaScript, on the other hand, allows for non-blocking code execution. 
 * It enables you to perform tasks that may take time to complete without freezing the user interface. 
 * Asynchronous code can be achieved using callbacks, promises, or async/await syntax. 
 * With asynchronous programming, you can initiate an operation and continue executing other 
 * code while waiting for the operation to complete. This leads to a more responsive and 
 * efficient application, as it can handle multiple tasks concurrently without blocking 
 * the main thread. **/

// Example of synchronous code
console.log("Synchronous code start");
for (let i = 0; i < 5; i++) {
    console.log(i);
}
console.log("Synchronous code end");

// Output:
// Synchronous code start
// 0    
// 1
// 2
// 3
// 4
// Synchronous code end

console.log("-".repeat(20)); // Separator for clarity
console.log("Ordering pizza...");

setTimeout(function(){
    console.log("Pizza is ready!");
}, 1000);

console.log("Doing homework while waiting...");

// Output:
// Ordering pizza...
// Doing homework while waiting...
// Pizza is ready! (after 1 second)
