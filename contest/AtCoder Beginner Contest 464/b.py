H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = []
if S[0] == "."*W:
    S.pop(0)
if S[-1] == "."*W:
    S.pop(-1)
for i in S:
    if i[0] == "." and i[-1] == ".":
        ans.append(i[1:-1])
print(*ans, sep="\n")