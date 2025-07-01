let arr = ["apple", "banana", "grape", "blueberry", "orange"];
const fs = require('fs');
let eng = fs.readFileSync(0).toString().trim();
let cnt = 0;

for (let i=0; i<arr.length;i++){
    if (arr[i][2]==eng || arr[i][3]==eng){
        console.log(arr[i]);
        cnt+=1;
    }
}
console.log(cnt);