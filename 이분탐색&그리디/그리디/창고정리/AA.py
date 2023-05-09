import sys
# sys.stdin = open('input.txt', 'rt')

n =int(input())

wareHouse = list(map(int, input().split()))

m = int(input())

wareHouse.sort()

# 하나 빼고 더할때마다, 최소값/최대값 각각을 비교해서, 만약 작거나 크면 최소/최대값 바꾸기

res = 0
for _ in range(m):
    wareHouse[0] += 1
    wareHouse[-1] -= 1
    wareHouse.sort()
    res = wareHouse[-1] - wareHouse[0]
print(res)