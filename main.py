n = int(input())
s = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        s.append(i)
        s.append(n//i)
for j in sorted(set(s)):
    print(j)