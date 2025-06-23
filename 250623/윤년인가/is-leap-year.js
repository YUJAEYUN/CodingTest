const fs = require('fs');
let y = Number(fs.readFileSync(0).toString().trim())

let flag;

if (y%4===0){
    flag = true;
    if (y%100===0 && y%400!==0){
        flag = false;
    }
    
}
else{
    flag = false;
}

console.log(flag? true : false);