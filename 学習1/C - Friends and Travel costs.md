# ABC203 C

## URL
https://atcoder.jp/contests/abc203/tasks/abc203_c

## 解答
```python
n, k = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
for i in sorted(s):
    if i[0] <= k:
        k += i[1]
    else:
        break
print(k)
```

## 方針
- 所持金で進めるだけ進み、途中経過する村で所持金を増やす
- これ以上進めなくなったら着地している場所を出力

## 解法ポイント
- 全探索するとLTEになるので、計算量を少なくする工夫が必要

## メモ
- 計算量はO(NlogN)
- 最初はbreakを入れなかったが、入れないと最後まで計算するので実行時間が長くなる(入れなくてAC)
