# ABC081A - Placing Marbles

## URL
https://atcoder.jp/contests/abs/tasks/abc081_a

## 解答
```python
s = list(input())
print(sum(int(i) for i in s))
```

## 方針
- 各桁の数を合計する

## 解法ポイント
- 入力は1 or 0なので合計した数を出力すればOK

## メモ
- print()内でforループができる
最初はこれで解答
```python
s = list(input())
ans = 0
for i in s:
    i = int(i)
    ans += i
print(ans)
```