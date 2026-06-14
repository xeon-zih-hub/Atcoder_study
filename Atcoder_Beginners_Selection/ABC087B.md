# ABC087B

## URL
https://atcoder.jp/contests/abs/tasks/abc087_b

## 解答
```python
A = int(input())
B = int(input())
C = int(input())
X = int(input())
ans = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if a*500 + b*100 + c*50 == X:
                ans += 1
print(ans)
```

## 方針
- forループで全探索

## 解法ポイント
- 制約0 <= A, B, C <= 50なので3重forループしても間に合う

## メモ
- 
