# B - Magic 3

## URL
https://atcoder.jp/contests/abc190/tasks/abc190_b

## 解答
```python
n, s, d = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    if x < s and d < y:
        print("Yes")
        exit()
print("No")
```

## 方針
- s未満のxと、dより大きいyが存在するかを全パターン調べる

## 解法ポイント
- 全探索を使う
- 制約条件1<=N<=100なので全パターンを試してもTLEしない

## メモ
-
