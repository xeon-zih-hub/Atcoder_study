# B - Alcoholic

## URL
https://atcoder.jp/contests/abc189/tasks/abc189_b

## 解答
```python
N, X = map(int, input().split())
ans = 0
for i in range(N):
    V, P = map(int, input().split())
    if ans + V*P > X*100:
        print(i+1)
        exit()
    ans += V*P
print(-1)
```

## 方針
- アルコール度数が基準値を超えたら酔うので、それ何杯目かを出力する

## 解法ポイント
- 割り算を使うと小数点の誤差が出る可能性があるので、極力小数が出てくる計算を避ける実装をする

## メモ
- 何杯目かを出力させるのを考えるのに苦労した
