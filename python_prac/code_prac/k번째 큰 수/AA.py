import sys
sys.stdin = open('input.txt', 'rt')

n,K = map(int, input().split())

cards = list(map(int, input().split()))

cards.sort(reverse=True)

res = set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            first = cards[i]
            second = cards[j]
            third = cards[k]
            res.add(first+second+third)


res = list(res)
res.sort(reverse=True)
print(res[K-1])
        