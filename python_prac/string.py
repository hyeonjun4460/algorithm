msg = 'It is Time'

# upper, lower : 원본은 유지된다.
a = msg.upper()
b = msg.lower()
print(a)
print(b)

# find 문자열에서 특정 문자를 찾고, 해당하는 문자가 위치한 가장 가까운 index를 출력한다.
print(a.find('I'))

# count: 특정 값의 개수를 센다.
print(a.count('T'))

# slice: 문자열 쪼개기
print(a[:2]) # 0번 인덱스부터 n-1까지 분리
print(a[3:5]) # 3번부터 4번까지 분리


# len: 문자열의 길이 출력
print(len(a))

# isupper, islower: 대/소문자 판별하여 boolean 값 출력
for i in a:
    if i.isupper():
        print('upper')

for i in a:
    if i.islower() == False:
        print('not lower')

# isalpha: 알파벳 판별하여 boolean 값 출력
for i in a: 
    if i.isalpha():
        print("alhpabet")
    else:
        print('공백')

# ord: 문자의 아스키넘버를 출력
# A~Z = 65 ~ 90
# a~z = 97 ~ 122
for i in a:
    print(ord(i))

# chr: 정수에 대응하는 아스키넘버의 문자열 출력
print(chr(65)) # A
