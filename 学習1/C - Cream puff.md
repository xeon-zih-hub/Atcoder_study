# ABC180 C

## URL
https://atcoder.jp/contests/abc180/tasks/abc180_c

## 解答
```python
n = int(input())
s = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        s.append(i)
        s.append(n//i)
for j in sorted(set(s)):
    print(j)
```

## 方針
-　

## 解法ポイント
-　

## メモ
-　
