# ABC049C - 白昼夢

## URL
https://atcoder.jp/contests/abs/tasks/arc065_a

## 解答
```python
s = input()
while s:
    flag = False
    for w in ("dream", "dreamer", "erase", "eraser"):
        if s.endswith(w):
            s = s[:-len(w)]
            flag = True
            break
    if not flag:
        print("NO")
        exit()
print("YES")
```

## 方針
- 文字列 S が dream, dreamer, erase, eraser の連結で作れるか判定する
- 前から見ると dream と dreamer が紛らわしいため、後ろから単語を削っていく
- 最後に文字列が空になれば YES、途中で削れなくなれば NO

## 解法ポイント
- s.endswith(w) で、文字列 s の末尾が単語 w と一致するか確認する
- 一致したら s = s[:-len(w)] で末尾の単語を削る
- 4単語すべて試しても削れない場合、その時点で作れないので NO
- while s: は「s が空文字列でない間続ける」という意味
- 後ろから処理することで、dream / dreamer、erase / eraser の曖昧さを避けられる

## メモ
- まったく方針がわからない
- 何をしたいのか理解するまでに時間がかかった
- 文字列の.endwith()を知らなかった
