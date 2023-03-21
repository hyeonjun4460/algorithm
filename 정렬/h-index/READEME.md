# 문제링크

- https://school.programmers.co.kr/learn/courses/30/lessons/42747#
  <br></br>

# 정답 풀이

- h-index는 인용수가 논문의 수보다 작아지기 시작하는 논문의 수이다.
- 배열에 인용수가 주어지므로, value가 index보다 작거나 같아지면 index 값을 answer로 return했다.
- value가 index보다 작거나 같아지는 시점이 없을 경우, 배열의 길이, 총 논문의 수를 return했다.
  <br></br>

# 해맨 이유

- h-index를 인용된 논문 수 - 인용되지 않은 논문 수의 값이 가장 작은 양수로 오해했다.
