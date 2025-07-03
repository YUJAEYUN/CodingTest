const fs = require('fs');
let N = Number(fs.readFileSync(0).toString().trim());

for (let i=1; i<=N; i++){
    let str = "";
    for (let j=0; j<2*i-1; j++){
        str += "*";
    }
    console.log(str);
}