const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split(' ');

let A = Number(input[0]);
let B = Number(input[1]);
let result1, result2;

if (A<B){
    result1 = 1, result2 = 0
}else{
    result1 = 0
    if (A===B){
        result2 = 1
    }
};

console.log(`${result1} ${result2}`);