// 정렬 알고리즘으로 풀었지만 A B C는 안쓰이는데 꼭 써야할까?
const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split(" ");

let A = Number(input[0]);
let B = Number(input[1]);
let C = Number(input[2]);

for (let i=0; i<2;i++){
    if (Number(input[i]) > Number(input[i+1])){
        [input[i], input[i+1]] = [input[i+1], input[i]];
    }
}

console.log((Number(input[0])<Number(input[1])? input[1]: input[0]));