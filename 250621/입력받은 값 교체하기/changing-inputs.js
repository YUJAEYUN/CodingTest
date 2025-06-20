const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(' ');

let a = Number(input[0]);
let b = Number(input[1]);

//값 교체 파이썬이랑 비슷
[a,b] = [b,a]

console.log(a, b)