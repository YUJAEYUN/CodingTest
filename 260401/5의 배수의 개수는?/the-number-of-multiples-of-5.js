const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(/\s+/).map(Number);
let cnt = 0;

for (let i=0;i<16;i++){
    if (input[i] % 5 ===0){
        cnt+=1;
        }
    }

console.log(cnt);