# B - Visibility

## URL
https://atcoder.jp/contests/abc197/tasks/abc197_b

## 解答
h, w, x, y = map(int, input().split())
s = [list(input()) for i in range(h)]
x -= 1
y -= 1
cnt = 1

i = y + 1
while i < w and s[x][i] == ".":
    cnt += 1
    i += 1
i = y - 1
while 0 <= i and s[x][i] == ".":
    cnt += 1
    i -= 1
i = x + 1
while i < h and s[i][y] == ".":
    cnt += 1
    i += 1
i = x - 1
while 0 <= i and s[i][y] == ".":
    cnt += 1
    i += 1
print(cnt)

## 方針
- (X,Y)のマスから上、下、右、左方向へ、壁に当たるまで何マス進めるかを調べる

## 解法ポイント
- whileを使って上、下、右、左方向の端にぶつかるまで、"#"にぶつかるまで調べる

## メモ
- IndexError: string index out of rangeのエラーが頻発する
- 上記エラーをうまく修正できず、解答を調べた
