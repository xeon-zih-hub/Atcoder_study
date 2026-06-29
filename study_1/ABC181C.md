# C - Collinearity

## URL
https://atcoder.jp/contests/abc181/tasks/abc181_c

## 解答
```python
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
                print("Yes")
                exit()
print("No")
```

## 方針
- 3つの座標が同じ直線状にあるかどうかを判定する

## 解法ポイント
- 座標1と座標2を結ぶ直線と座標1と座標3を結ぶ直線の傾きが同じかどうかを判定すればよい

## メモ
- 直線の傾き以外にもベクトルでの解法もあるが、よく理解できなかったのでスルーした
