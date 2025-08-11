const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split(" ");
let start = Number(input[0]);
let end = Number(input[1]);
let result = 0


function check(number){
    let cnt = 0;
    for(let i=1;i<=number;i++){
        if (number%i===0){
            cnt+=1;
        }
    }
    if (cnt === 3){
        return true;
    }
}

for (let j = start; j<=end; j++){
    if (check(j)){
        result+=1;
    }
}

console.log(result);