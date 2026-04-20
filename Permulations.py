from itertools import permutations
def solve():
    try:
        line = input().split()
        if not line:
            return
        S = line[0]
        K = int(line[1])
        sorted_S = sorted(S)
        perms = permutations(sorted_S, K)
        for p in perms:
            print("".join(p))
    except (EOFError, ValueError, IndexError) as e:
        pass
if __name__ == "__main__":
    solve()
