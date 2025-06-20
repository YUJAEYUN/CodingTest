const fs = require('fs');
let N = Number(fs.readFileSync(0).toString().trim());

// console.log(N >=80? 'pass': `${80-N} more score`); 이렇게도 됨

if (N>=80){
    console.log('pass')
} else{
    console.log(`${80-N} more score`)
}