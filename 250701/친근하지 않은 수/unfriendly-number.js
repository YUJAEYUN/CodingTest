const fs = require('fs');
let N = Number(fs.readFileSync(0).toString().trim());
let cnt = N;

for (let i=N;i>0;i--){
    if (i%2===0 || i%3===0 || i%5===0){
        cnt-=1
    }
}
console.log(cnt);