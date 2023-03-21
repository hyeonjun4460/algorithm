// 정답
function solution(citations) {
    citations.sort((a, b) => { return b - a })
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] > i) {
            continue
        } else {
            return i
        }
    }
    return citations.length
}

// 오답
function solution(citations) {
    var answer = 0;
    //     h번 이상 인용된 논문 수
    //     h번 이하 인용된 논문 수
    //     h번 이상 인용된 논문 수 - h번 이하 연용된 논문 수의 절대값이 가장 작은 것
    //     절대값이 같은 논문이 있다면, 양수가 answer
    const hIndex = []
    for (let i = 0; i < citations.length; i++) {
        let up = 0
        let down = 0
        for (let j = 0; j < citations.length; j++) {
            if (citations[i] <= citations[j]) {
                up += 1
            } else {
                down += 1
            }
        }
        hIndex.push({ index: i, point: up - down })
    }
    hIndex.sort((a, b) => {
        return Math.abs(a.point) - Math.abs(b.point)
    })
    console.log(hIndex)
    return citations[hIndex[0].index];
}