const fs = require("fs");
// split 함수를 이용해 여러 줄 입력받기
let input = fs.readFileSync(0).toString().trim().split('\n');


let a = Number(input[0]).toFixed(3);
let b = Number(input[1]).toFixed(3);
let c = Number(input[2]).toFixed(3);


console.log(a);
console.log(b);
console.log(c);