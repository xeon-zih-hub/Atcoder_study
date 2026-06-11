# ABC186 C

## URL
https://atcoder.jp/contests/abc186/tasks/abc186_c

## 解答
```python
n = int(input())


def judge_10(x):
    return not "7" in str(x)


def judge_8(x):
    s = ""
    while 0 < x:
        s = str(x%8) + s
        x //= 8
    return not "7" in s


cnt = 0
for i in range(1, n+1):
    if judge_10(i) and judge_8(i):
        cnt += 1
print(cnt)
```

## 方針
-　nを10進数表示と8進数表示にしたとき、7を含むかどうかを判定し含まない数を出力する

## 解法ポイント
-　10進数をN進数にする場合： 1. Nで割った余りを上の桁につける 2. Nで割った商に置き換える
- 上記の操作を0になるまで繰り返す

## メモ
-　oct(x)で一発で計算できる
- judge_8の関数を作成するとき、whileの条件づけに苦戦した