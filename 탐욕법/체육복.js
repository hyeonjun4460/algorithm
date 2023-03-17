// 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42862
// 문제 해결 포인트
// - lost, reserve 중복 제거
// - 중복 제거 후 lost 정렬
// - lost에서 reserve 탐색 시, 순서는 작은거부터
function solution(n, lost, reserve) {
    //     reserve - lost 겹치면 빼기
    lost = lost.filter((value) => {
        if (reserve.includes(value)) {
            reserve[reserve.indexOf(value)] = 100
        } else {
            return value
        }
    })

    var answer = n - lost.length
    //     체육복 빌리는 인원을 sort 해주어야, reserve에서 순차적으로 체육복을 빌릴 수 있음.
    lost = lost.sort((a, b) => { return a - b })
    //     체육복을 빌리는 순서는 작은거부터 순서대로.
    for (let i = 0; i < lost.length; i++) {
        const student = lost[i]
        if (reserve.includes(student - 1)) {
            answer += 1
            reserve[reserve.indexOf(student - 1)] = 100
            continue
        }
        else if (reserve.includes(student + 1)) {
            answer += 1
            reserve[reserve.indexOf(student + 1)] = 100
        }
    }
    return answer
}