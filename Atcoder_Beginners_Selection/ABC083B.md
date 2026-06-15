# ABC083B - Some Sums

## URL
https://atcoder.jp/contests/abs/tasks/abc083_b

## 解答
```python
N, A, B = map(int, input().split())
ans = 0
for i in range(1, N+1):
    if A <= sum(int(j) for j in list(str(i))) <= B:
        ans += i
print(ans)
```

## 方針
- 1からNまでの数の各桁の和を計算して、条件にあったものを足し合わせて出力する

## 解法ポイント
- 一度文字列に変換すると各桁に分解できる
- 条件判定したあとに整数に直して合計する

## メモ
- 何回も解いたが結構解法を忘れる
- どのタイミングで文字列にして、どのタイミングで整数に戻すか
