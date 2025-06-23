const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split("\n");

let A = input[0].split(" ");
let B = input[1].split(" ");

let mathA = Number(A[0]), engA = Number(A[1]);
let mathB = Number(B[0]), engB = Number(B[1]);

if (mathA > mathB && engA > engB){
    console.log(1);
}
else{
    console.log(0);
}