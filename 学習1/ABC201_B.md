# B - Do you know the second highest mountain?

## URL
https://atcoder.jp/contests/abc201/tasks/abc201_b

## 解答
n = int(input())
li = []
for i in range(n):
    s, t = input().split()
    li.append([int(t), s])
print(sorted(li, reverse=True)[1][1])

## 方針
- 高さを並び替えて、2番目に高い山の名前を出力する

## 解法ポイント
- リスト内の要素を降順でソートする
- 2次元配列の場合、先頭の要素に沿ってソートされる

## メモ
- 最初li.append([t, s])で提出したらWAになった
- tを文字列のままにしていると、sorted(["10", "2"])は["10", "2"]で出力される。文字列では1が2よりも先に来るからである
