# ABC085B - Kagami Mochi

## URL
https://atcoder.jp/contests/abs/tasks/abc085_b

## 解答
```python
N = int(input())
D = [int(input()) for _ in range(N)]
print(len(set(D)))
```

## 方針
- ユニークな値が何個存在するかを数えればよい

## 解法ポイント
- 入力をリスト型にし、そのあと重複を取り除くようset型に変換
- set内の個数を出力する

## メモ
- 
