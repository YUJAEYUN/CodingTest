const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');
let idx = 0;
while (true){
    num = Number(input[idx]);
    idx++;
    if (num<25){
        console.log("Higher");
    }
    else if (num>25){
        console.log("Lower");
    }
    else{
        console.log("Good");
        break;
    }
}