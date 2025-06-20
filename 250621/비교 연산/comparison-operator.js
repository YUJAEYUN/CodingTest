const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split(' ');

let a = Number(input[0]);
let b = Number(input[1]);

// 삼항연산자로 할 수 있었네
console.log(a >= b ? 1 : 0);
console.log(a > b ? 1 : 0);
console.log(a <= b ? 1 : 0);
console.log(a < b ? 1 : 0);
console.log(a == b ? 1 : 0);
console.log(a != b ? 1 : 0);