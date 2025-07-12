const fs = require('fs');
let N = Number(fs.readFileSync(0).toString().trim());

for (let i=1;i<=N;i++){
    str="";
    for (let j=1;j<=N;j++){
        if(j===N){
            str += `${i} * ${j} = ${i*j}`
        }
        else{
        str += `${i} * ${j} = ${i*j}, `
        }
    }
    console.log(str);
}