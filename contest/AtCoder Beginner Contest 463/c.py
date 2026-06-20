N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
T = list(map(int, input().split()))
for t in T:
    ans = []
    for i in li:
        if t+0.5 < i[1]:
            ans.append(i[0])
    print(max(ans))