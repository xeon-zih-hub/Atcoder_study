# ABC192 C

## URL
https://atcoder.jp/contests/abc192/tasks/abc192_c

## 解答
```python
n, k = map(int, input().split())

def g1(n):
    n = list(str(n))
    s = "".join(sorted(n, reverse=True))
    return int(s)


def g2(n):
    n = list(str(n))
    s = "".join(sorted(n))
    return int(s)


def f(n):
    return g1(n) - g2(n)


for i in range(k):
    n = f(n)
print(n)
```

## 方針
-　指示通りの処理を行う関数を作成する

## 解法ポイント
-　

## メモ
-　s="".join()をあまり理解できていない気がする
- https://note.nkmk.me/python-string-concat/#join