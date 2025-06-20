const fs = require("fs");
let result = fs.readFileSync(0).toString().trim();

console.log(`Your score is ${result} point.`);