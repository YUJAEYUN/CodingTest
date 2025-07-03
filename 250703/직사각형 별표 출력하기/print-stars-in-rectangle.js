const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split(" ");

let N = Number(input[0]);
let M = Number(input[1]);

for (let i=0; i<N; i++){
    let result = "";

    for (let j=0; j<M; j++){
        result += "* ";
    }
    console.log(result);
}