M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))
sym_diff = a.symmetric_difference(b)
for item in sorted(list(sym_diff)):
    print(item)