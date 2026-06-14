# ABC081B - Shift only

## URL
https://atcoder.jp/contests/abs/tasks/abc081_b

## 解答
```python
N = int(input())
A = list(input().split())
cnt = 0
while all(int(i) % 2 == 0 for i in A):
    cnt += 1
    A = [int(i) // 2 for i in A]
print(cnt)
```

## 方針
- 2で割り切れないまでループ計算する

## 解法ポイント
- 1個でも偶数でなくなったときに終了

## メモ
- all()の使い方を学んだ
