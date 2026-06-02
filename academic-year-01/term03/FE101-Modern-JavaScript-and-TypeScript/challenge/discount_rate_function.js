/// Course: FE 101  - Introduction to Modern JavaScript and TypeScript
/// Week 02: JavaScript Data & Logic
/// Topic: Challenge - higher order functions and callbacks
/// Date: May 31, 2026

// Create a function called discountRate that takes a price and a discount percentage, 
// and returns the discounted price.

// Then create a higher-order function called applyDiscount 
// that takes an array of products and a discount function,
const applyDiscount = (items, fn) => items.map(fn);

//ceate a function called makeDiscount that takes a discount percentage and 
// returns a function that applies that discount to a product object, 
// returning a new product object with the discounted price.
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