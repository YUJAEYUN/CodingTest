const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');

let N = Number(input[0]);
let arr = input[1].split(" ");
result = "";

for (let i=0; i<N; i++){
    result += (Number(arr[i])**2+" ");
}
console.log(result);