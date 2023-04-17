import sys
# sys.stdin = open('input.txt', 'rt')

N = int(input())

for n in range(1,N+1):
    textList = list(map(lambda x: x.lower(),input()))
    reverseList = textList.copy()
    reverseList.reverse()
    text = ''.join(textList)
    reverseText = ''.join(reverseList)
    answer = '#'+str(n)
    if text == reverseText:
        answer += ' ' + 'YES'
    else:
        answer += ' ' + 'NO'
    print(answer)
