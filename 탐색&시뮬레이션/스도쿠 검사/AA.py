import sys
sys.stdin = open('input.txt', 'rt')

sudoku = list()

for _ in range(9):
    # 행 검사
    origin = list(map(int, input().split()))
    setOrigin = set(origin)
    if len(origin) == len(setOrigin):
        sudoku.append(list(map(int, origin)))
    else:
        print('NO')
        break

# 열 검사
for i in range(len(sudoku)):
    columnList = list()
    for j in range(len(sudoku)):
        columnList.append(sudoku[i][j])
    columnSet = set(columnList)
    if len(columnList) != len(columnSet):
        print('NO')
        break

for i in range(0,len(sudoku),3):
    threeList = list()
    for j in range(i,i+3):
        threeList += [sudoku[j][i], sudoku[j][i+1], sudoku[j][i+2]]
    threeSet = set(threeList)
    if len(threeList) != len(threeSet):
        print('NO')
        break
else:
    print('YES')


# 3*3 검사