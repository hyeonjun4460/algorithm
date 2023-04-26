import sys
# sys.stdin = open('input.txt', 'rt')

procession = list()
for _ in range(7):
    procession.append(list(map(int, input().split())))

# print(procession)

def test(list):
    for i in range(5//2):
        if list[i] != list[-1-i]:
            return False
    else:
        return True

cnt = 0
for i in range(len(procession)):
    column = list()
    # 열 생성
    for k in range(len(procession)):
        column.append(procession[k][i])
    for j in range(3):
        # 행 생성
        row = procession[i][j:j+5]
        testColumn = column[j:j+5]
        if test(row):
            cnt +=1
        if test(testColumn):
            cnt+=1
        

print(cnt)



        
# 열검사