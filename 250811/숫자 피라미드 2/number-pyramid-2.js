const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();

let N = Number(input[0]);
let num = 1;

for (let i=1;i<=N;i++){
    let result="";
    for (let j=0; j<i; j++){
        result += `${num} `
        num+=1;
    }
    console.log(result);
}