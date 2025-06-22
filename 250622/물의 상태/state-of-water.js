const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();

let n = Number(input);

if (n<0){
    console.log('ice')
}else if (n>=100){
    console.log('vapor')
}else{
    console.log('water')
}