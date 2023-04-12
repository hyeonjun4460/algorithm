import random as r

# 리스트 선언
a = []
b = list()

# 리스트 합치기
a = [1,2,3]
b = list([4,5,6])

c = a+b
print(c)

# append: 마지막 index에 값 추가
c.append(7)

# insert: 특정 index에 값 추가
c.insert(0, 100) 

print(c) # [100, 1, 2, 3, 4, 5, 6, 7]

#pop: index 제거 (default: 마지막 인덱스)
c.pop()
c.pop(1)
print(c) # # [100, 2, 3, 4, 5, 6]

# remove: 특정 값 제거
c.remove(4)
print(c) # # [100, 2, 3, 5, 6]

# index: 값의 index 출력
print(c.index(100)) # 0

# sum: 정수/실수 원소들의 합을 출력
print(sum(list(range(1,11)))) # 55

# max, min: 최대, 최소 출력
print('max :', max(c), 'min: ', min(c)) # 100, 2

# sort: 리스트를 특정 순서로 정렬 default: 오름차순(원본에 영향)
r.shuffle(a)
print(a) 
a.sort()
print(a)  # 1,2,3
a.sort(reverse=True)
print(a) # 3,2,1

# claer: 리스트 값 삭제 (원본에 영향)
a.clear()
print(a)

# copy, [:] : 리스트 깊은 복사 
c = [1,2,3,4,5]
d = c.copy()
c[0] = 0
print(d) # [1, 2, 3, 4, 5] (깊은 복사)
d = c[:]
c[0] = 1
print(d) # [0, 2, 3, 4, 5] (깊은 복사)