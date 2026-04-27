from collections import defaultdict
n_m = list(map(int, input().split()))
n = n_m[0]
m = n_m[1]
d = defaultdict(list)
for i in range(n):
    word = input()
    d[word].append(i + 1)
for i in range(m):
    word = input()
    if word in d:
        print(" ".join(map(str, d[word])))
    else:
        print("-1")
