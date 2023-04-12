# slice: 리스트를 특정 index를 기준으로 분리
a = [1,2,3,4,5]
b = a[:3]
c = a[1:2]
print(b) # 1,2,3
print(c) # 2,3,

# len: 배열의 길이, 값 개수
print(len(a))

# 원소에 접근
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)

# enumerate: list, tuple, string 자료형의 각 index에 할당된 값을 (index, value) 형태의 enumerate 객체로 변환.

for i in enumerate(a):
    print(i, end=' ') # (0, 1) (1, 2) (2, 3) (3, 4) (4, 5)

# a = index, b = value
for a, b in enumerate(a):
    print(a, ': ',b)


# all: 반복 가능한 객체를 매개변수로 받아, 조건에 모두 부합하면 boolean 반환
# 이 때, 매개변수에는 반복 가능한 객체와 더불어 조건문을 약식으로 걸 수 있다.
list = list(range(10))
print(all([True,True,True])) # true
print(all([True,False,True])) # false
print(all(x>5 for x in list)) # false
print(any(x>5 for x in list)) # true

if all(x>10 for x in list):
    print('yes')
else:
    print('no')
# any: 반복 가능한 객체를 매개변수로 받아, 하나라도 조건에 부합하면 boolean 반환
if any(x>5 for x in list):
    print('yes')
else:
    print('no')