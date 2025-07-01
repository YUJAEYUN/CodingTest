const fs = require('fs');
let N = Number(fs.readFileSync(0).toString().trim());

let tmp = 1;
let i = 1;

while (tmp<=N){
    tmp+=i;
    i++;
}
console.log(i-1);