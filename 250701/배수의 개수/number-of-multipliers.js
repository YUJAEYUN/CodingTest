const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');
let result1 = 0;
let result2 = 0;

for (let i = 0; i<input.length;i++){
    if (Number(input[i])%3===0){
        result1+=1;
    }
    if (Number(input[i]%5===0)){
        result2+=1;
    }
}
console.log(result1, result2)