// 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/42883#
// 정답
// 핵심1: stack에 넣을 값을 stack의 기존 값들과 비교하여, 기존 값이 넣을 값보다 클 때까지 pop을 해준다.(가장 큰 값이 stack의 첫번째 값이 된다)
// 핵심2: 자리수를 number.length-k와 맞추기 위해, stack을 마지막으로 splice로 k개 만큼 뒤에서부터 삭제한다.
function solution(number, k) {
    const stack = []
    for (let i = 0; i < number.length; i++) {
        while (k > 0 && stack[stack.length - 1] < number[i]) {
            stack.pop()
            k--
        }
        stack.push(number[i])
    }
    stack.splice(stack.length - k, k)
    return stack.join('')
}
// 오답 풀이
// 오답이유1: stack에 넣는 number 값의 비교는 stack의 모든 값들과 해야하는데, stack의 가장 최근값만 했다.
// 오답이유2 결과 값의 자리수는 number의 length -k로 일치해야한다.
function solution(number, k) {
    const stack = []
    let count = 0
    number = number.split('')
    for (let i = 0; i < number.length; i++) {
        if (count === k) {
            stack.push(...number.slice(i))
            while (stack.length !== number.length - k) {
                stack.pop()
            }
            break
        }
        //         넣을 값 비교
        if (stack[stack.length - 1] < number[i]) {
            stack.pop()
            stack.push(number[i])
            count++
        } else {
            stack.push(number[i])
        }
        //         기존 값 비교
        if (stack[stack.length - 2] < stack[stack.length - 1]) {
            stack.shift()
            count++
        }
        if (i === number.length - 1 && count < k) {
            stack.push(...number.slice(i))
            while (stack.length !== number.length - k) {
                stack.pop()
            }
        }
    }

    return stack.join('')
}