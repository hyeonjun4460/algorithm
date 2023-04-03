// 1. 큰수의 법칙
// 숫자 n,m,k가 주어진다.
// n은 배열의 크기, m은 덧셈 횟수, k는  특정 인덱스 값을 더할 수 있는 횟수 제한 수를 의미한다.
// n 크기의 배열이 list로 주어질 때, n,m,k에 따른 큰 수의 법칙의 결과를 출력하라.

const n = 5
const m = 8
const k = 3

var list = '2 4 5 4 6'

// expect: 46

list = list.split(' ').map((value) => {
    return Number(value)
})

list.sort((a, b) => {
    return b - a
})
let count = 0
let result = 0
let sumCount = 0
const a = list[0]
const b = list[1]
console.log(a, b)
while (sumCount < m) {
    if (count !== k) {
        result += a
        count += 1
    } else {
        result += b
        count = 0
    }
    sumCount += 1
}

console.log(result) // 46

