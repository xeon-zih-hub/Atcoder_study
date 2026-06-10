# ABC188 B

## URL
https://atcoder.jp/contests/abc188/tasks/abc188_b

## 解答
```python
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
for i in range(n):
    s += a[i] * b[i]
print("Yes" if s == 0 else "No")
```

## 方針
- リストでA,Bを受け取り、forループで1個ずつAの要素とBの要素の積を求めて足していった

## 解法ポイント
-

## メモ
リスト内包表記で書けた
---------------------------------------------
s = [a[i] * b[i] for i in range(n)]
print("Yes" if sum(s) == 0 else "No")