import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

for n in range(1,N+1):
    textList = list(map(lambda x: x.lower(),input()))
    reverseList = textList.copy()
    reverseList.reverse() # s[::-1]
    text = ''.join(textList)
    reverseText = ''.join(reverseList)
    if text == reverseText:
        print("#%d YES" %n)
    else:
        print("#%d NO" %n)
