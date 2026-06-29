# ABC086C - Traveling

## https://atcoder.jp/contests/abs/tasks/arc089_a


## 解答
```python
N = int(input())
pt, px, py = 0, 0, 0
flag = "Yes"
for i in range(N):
    t, x, y = map(int, input().split())
    dist = abs(px-x) + abs(py-y)
    dt = t - pt
    if dist > dt or (dt - dist) % 2 != 0:
        flag = "No"
        break
    pt, px, py = t, x, y
print(flag)
```

## 方針
- 各予定 (t, x, y) に対して、前の地点からその時刻までに到達できるかを順番に判定する
- 移動距離はマンハッタン距離 abs(x - px) + abs(y - py) で求める
- 1つでも到達不可能な予定があれば No
- 全て到達可能なら Yes

## 解法ポイント
- 使える時間は dt = t - pt
- 必要な最短移動距離は dist = abs(x - px) + abs(y - py)
- dist > dt なら時間が足りないので不可能
- (dt - dist) % 2 != 0 なら余った時間の偶奇が合わないので不可能
- 各予定を処理したら、現在地と現在時刻を pt, px, py = t, x, y に更新する

## メモ
- 
