const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');

let numCount = Number(input[0]);
let arr = "";
arr = input[1].split(" ");
result = "";
for (let i=numCount-1; i>=0;i--){
    if (arr[i]%2===0){
        result += `${arr[i]} `;
    }
}
console.log(result);