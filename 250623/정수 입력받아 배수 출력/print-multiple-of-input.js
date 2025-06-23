const fs = require('fs');
let N = Number(fs.readFileSync(0).toString().trim());
result = "";

for (let i = 1; i < 6; i++){
    result += (i*N+" ");
}

console.log(result);