# ABC180 C

## URL
https://atcoder.jp/contests/abc180/tasks/abc180_c

## 解答
```python
n = int(input())
s = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        s.append(i)
        s.append(n//i)
for j in sorted(set(s)):
    print(j)
```

## 方針
- 割り切れる数を出力する

## 解法ポイント
- 制約条件によると1<=N<=10^12なので、全探索したら間に合わない
- 素数かどうかを判定する方法を利用して計算量をO(√N)に抑える

## メモ
- 重解をもつとき、2つとも出力されるのでWAになる(ex: 16を4で割ると4になり、リストには4が2つ入る)
- ユニーク値を出力させたいのでset型になおす