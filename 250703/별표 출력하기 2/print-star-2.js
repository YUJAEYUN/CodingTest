const fs = require('fs');
let N = Number(fs.readFileSync(0).toString().trim());

for (let i=N; i>0; i--){
    let str = "";
    for (let j=i; j>0; j--){
        str +="* ";
    }
    console.log(str);
}