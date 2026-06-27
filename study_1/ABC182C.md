# C - To 3

## URL
https://atcoder.jp/contests/abc182/tasks/abc182_c

## 解答
```python
n = input()

cnt = [0, 0, 0]

for c in n:
    cnt[int(c) % 3] += 1

s = sum(int(c) for c in n)
r = s % 3
l = len(n)

if r == 0:
    print(0)
elif r == 1:
    if cnt[1] >= 1 and l >= 2:
        print(1)
    elif cnt[2] >= 2 and l >= 3:
        print(2)
    else:
        print(-1)
else:
    if cnt[2] >= 1 and l >= 2:
        print(1)
    elif cnt[1] >= 2 and l >= 3:
        print(2)
    else:
        print(-1)
```

## 方針
- 

## 解法ポイント
- 

## メモ
- 
