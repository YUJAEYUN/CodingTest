const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split(" ");
let A = Number(input[0]);
let B = Number(input[1]);
let result = "";
while (A<=B){
    result += `${A} `;
    (A%2!==0? A*=2: A+=3);
}
console.log(result);