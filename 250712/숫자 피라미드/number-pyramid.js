const fs = require('fs');
let N = Number(fs.readFileSync(0).toString().trim());

for (let i=1;i<=N;i++){
    str="";
    for (let j=1;j<=i;j++){
        str+= `${i} `;
    }
    console.log(str);
}