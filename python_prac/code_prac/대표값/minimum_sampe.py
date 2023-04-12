a = [7,8,6,5,4,7,8,9,2]
tmp = float('inf') # 파이썬에서 가장 큰 실수값(8비트)

# 최소갑 기본 알고리즘
# 특정 조건의 충족을 반복문 순회하면서 지속 체크할 때 유용
for x in a:
    if x < tmp:
        tmp = x
print(tmp)
print(min(a)) # 동일