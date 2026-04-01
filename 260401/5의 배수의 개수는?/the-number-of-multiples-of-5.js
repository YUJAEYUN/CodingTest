const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split("\n");
let cnt = 0;

for (i=0;i<4;i++){
    for(j=0;j<4;j++){
        if (input[i][j] % 5 ==0){
            cnt+=1;
        }
    }
}

console.log(cnt);