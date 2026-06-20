N, X = input().split()
s = [input() for _ in range(int(N))]
sheets = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
for i in s:
    if i[sheets[X]] == "o":
        print("Yes")
        exit()
print("No")