if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
    runner_up=arr[-2]
    print(runner_up)
