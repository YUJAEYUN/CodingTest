const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split('\n');
let N = Number(input[0]);

for (let i=1;i<=N;i++){
    let arr = input[i].split(" ");
    let A = Number(arr[0]);
    let B = Number(arr[1]);
    let sum = 0;
    for (let j=A;j<=B;j++){
        if (j%2==0){
            sum+=j;
        }
    }
    console.log(sum);
}