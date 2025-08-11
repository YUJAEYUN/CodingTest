const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();

let N = Number(input); // input은 문자열이므로 Number()를 사용하여 숫자로 변환합니다.
let num = 1;

for (let i = 1; i <= N; i++) {
    let result = ""; // result 변수를 각 반복마다 초기화해줍니다.
    for (let j = 0; j < i; j++) {
        result += `${num} `;
        num++;
    }
    console.log(result);
}