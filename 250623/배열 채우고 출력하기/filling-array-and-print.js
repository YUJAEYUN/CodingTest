let A = [];

const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();
let arr = input.split(" ");
let tmp;
result = ""

for (let i=0;i<10;i++){
    tmp = arr.pop();
    result += tmp;
}
console.log(result);

