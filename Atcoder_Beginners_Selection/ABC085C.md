# ABC085C - Otoshidama

## URL
https://atcoder.jp/contests/abs/tasks/abc085_c

## 解答
```python
N, Y = map(int, input().split())
for i in range(N+1):
    for j in range(N+1-i):
        k = N - i - j
        if i*10000 + j*5000 + k*1000 == Y:
            print(f"{i} {j} {k}")
            exit()
print("-1 -1 -1") 
```

## 方針
- 全探索して該当するものが1個であればそれを出力する

## 解法ポイント
- 愚直にやる

## メモ
- Nが2000以下なので3重forループしても間に合うが、i, jが決まればkは一意に決まるので3重にする必要はない
- 出力は指定の仕様に気を付けること