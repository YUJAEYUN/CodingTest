const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();

let n = Number(input);

if (n>=3000){
    console.log('book')
}else if (1000<=n && n<3000){
    console.log('mask')
}else{
    console.log('no')
}