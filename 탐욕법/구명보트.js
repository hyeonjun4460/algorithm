// 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42885

// 문제 핵심
// - 구명보트에는 최대 2명까지만 탈 수 있다.


// 어려움을 겪은 부분
// 배열의 양 끝 value들을 더해주는 로직을 구현하는데 본의아니게 시간이 오래 걸렸다.
// for 문만 계속 쓰다시피하다보니, while문을 사용할 생각을 못했다.
// 구현 방법에 대해 좀 더 유연한 접근의 필요성을 느꼈다.
// 구현에 대한 유연한 접근을 위해서, js의 다양한 내부 함수들을 알고 있어야 될 필요도 느꼈다.
function solution(people, limit) {
    var answer = 0;
    //     큰 사람, 작은 사람을 더한다.
    //     만약 값이 더 크면, 큰 사람을 뺀다.

    people = people.sort((a, b) => {
        return a - b
    })
    let i = 0 // 큰거
    let j = people.length - 1 //작은거
    while (i <= j) {

        const sum = people[i] + people[j]
        // 구명보트 크기에 두 사람이 맞으면, 두 사람은 통과
        if (sum <= limit) {
            answer += 1
            i += 1
            j -= 1
        } else {
            // 구명보트 크기에 두 사람이 맞지 않으면, 무거운 사람만 통과
            answer += 1
            j -= 1
        }
    }
    return answer
}