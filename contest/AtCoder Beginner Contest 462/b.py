n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
li = []
for i, v in enumerate(s):
    print(i+1, v[1:])