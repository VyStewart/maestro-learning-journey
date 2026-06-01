/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Challenge - higher order functions and callbacks
/// Date: May 31, 2026

// Create a function called discountRate that takes a price and a discount percentage, 
// and returns the discounted price.
const applyDiscount = (items, fn) => items.map(fn);
function makeDiscount(rate) {
    return product => ({
        ...product,
        price: product.price * ( 1 - rate)
    });
}

const products = [
  { name: "Laptop", price: 1000, stock: 10 },
  { name: "Mouse", price: 40, stock: 50 },
  { name: "Keyboard", price: 75, stock: 30 }
];

const discount20 = makeDiscount(0.2);
const discountedProducts = applyDiscount(products, discount20);

console.log("Original:", products);
// Output: Original: [ { name: 'Laptop', price: 1000, stock: 10 }, { name: 'Mouse', price: 40, stock: 50 }, { name: 'Keyboard', price: 75, stock: 30 } ]
console.log("Discounted:", discountedProducts);
// Output: Discounted: [ { name: 'Laptop', price: 800, stock: 10 }, { name: 'Mouse', price: 32, stock: 50 }, { name: 'Keyboard', price: 60, stock: 30 } ]