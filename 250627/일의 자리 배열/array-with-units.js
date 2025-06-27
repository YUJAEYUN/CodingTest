const fs = require('fs');
let arr = fs.readFileSync(0).toString().trim().split(" ");
let result = `${arr[0]} ${arr[1]} `;

for (let i=0; i<8; i++){
    tmp = (Number(arr[i]) + Number(arr[i+1]))<10? (Number(arr[i]) + Number(arr[i+1])):(Number(arr[i]) + Number(arr[i+1]))-10;
    arr.push(tmp);
    result += (tmp+" ");
    tmp = 0;
}
console.log(result);