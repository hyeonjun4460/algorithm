import sys
sys.stdin=open("input.txt", "r")
s=input()
stack=[]
cnt=0
# 막대기를 만들고 막대기 안에 있는 레이저의 개수만큼 쪼개진 막대기 개수를 구하려함.
# 그래서 ()가 레이저인지, 막대기인지를 구분하는 것까지는 가능했지만, 로직이 매우 복잡해짐.
# 심플하게 레이저가 닿는 막대기의 개수 = 현재 스택에 있는 (의 개수로 생각하고, () 레이저가 생길 때마다 len의 길이만큼 잘라주면 풀이가 쉬움.
for i in range(len(s)):
    print(stack,cnt)
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        # 이전 것과 비교하는 이유는, 막대기가 하나 끊기는 지점인지 여부를 판단하기 위함.
        # )인 경우에는 막대기가 끊긴 것이므로, 잘린 막대기는 1개만 생긴다. 레이저가 생기진 않는다.
        if s[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)