# ABC088B - Card Game for Two

## URL
https://atcoder.jp/contests/abs/tasks/abc088_b

## 解答
```python
N = int(input())
A = list(map(int, input().split()))
alice = sum(sorted(A, reverse=True)[::2])
bob = sum(sorted(A, reverse=True)[1::2])
print(alice-bob)
```

## 方針
- カードをリストに格納し、降順にソートする
- リストから1個ずつ取得してその合計の差を出力する

## 解法ポイント
- リストの要素を1個飛ばして取得する必要がある

## メモ
- リストのスライスを覚える
- [スタート位置 : ゴール位置 : ステップ(間隔)]のステップで2を指定することで2個ずつ進む(1個飛ばし)
