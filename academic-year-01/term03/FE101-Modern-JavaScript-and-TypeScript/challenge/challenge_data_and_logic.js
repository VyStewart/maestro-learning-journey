/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Challenge - focus on for loops, while loops, and destructuring
/// Date: May 31, 2026

// Create an array with at least 3 product objects, each like { name, price, stock }.
// Then write one line using destructuring to grab the first product’s name and the last product’s stock, assigning them to firstName and lastStock.
const products = [
    { name: "Laptop", price: 1000, stock: 10 },
    { name: "Mouse", price: 40, stock: 50 },
    { name: "Keyboard", price: 75, stock: 30 }
];

const [{ name: firstName }, { stock: lastStock }] = products;
console.log(`First Product Name: ${firstName}, Last Product Stock: ${lastStock}`);
// Output: First Product Name: Laptop, Last Product Stock: 30   

console.log("Products:", products); 
//output: Products: [ { name: 'Laptop', price: 1000, stock: 10 }, { name: 'Mouse', price: 40, stock: 50 }, { name: 'Keyboard', price: 75, stock: 30 } ]

console.log ("-".repeat(20)); // Separator for clarity
/* Using alias and copy to modify the original array */
const techProducts = [
    { name: "Laptop", price: 1000, stock: 10 },
    { name: "Mouse", price: 40, stock: 50 },
    { name: "Keyboard", price: 75, stock: 30 }
];

const alias = techProducts;

/* Create a deep copy of the techProducts array using map and spread operator to copy 
/* each product object to ensure that modifications to the copy do not affect the original array.*/
const deepCopy = techProducts.map(product => ({...product}));

alias[0].price = 1200;
deepCopy[0].price = 1400;


console.log("Products:", techProducts);
console.log("Alias:", alias);
console.log("Copy:", deepCopy);




