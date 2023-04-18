import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

for n in range(N):
    text = input()
    text.upper()
    for i in range(len(text)//2):
        if(text[i] != text[-1-i]):
            print('#%d NO' %(n+1))
            break
    else:
        print('#%d YES' %(n+1))