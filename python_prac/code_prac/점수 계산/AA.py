import sys
# sys.stdin = open('input.txt', 'rt')

N = int(input())
scoreList = list(map(int, input().split()))

score_before = 0
answer=0
for score in scoreList:
    if score == 1:
        if score_before != 0:
            answer += score + score_before
            score_before += 1
        else:
            answer += 1
            score_before = 1
    else:
        score_before =0
print(answer)
            

