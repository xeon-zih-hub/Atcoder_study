# ABC191 B

## URL
https://atcoder.jp/contests/abc191/tasks/abc191_b

## 解答
```python
n, x = map(int, input().split())
a = list(map(int, input().split()))
s = [i for i in a if i != x]
print(*s)
```

## 方針
- 入力をリストで受け取り、その要素からxと異なるものを新たなリストに追加して出力

## 解法ポイント
- 出力時にリスト前に*"をつけないとWAになる

## メモ
- リストそのものではなく、リストの要素を出力するときは*をつけること