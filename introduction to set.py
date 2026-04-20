def average(arr):
    distinct_heights = set(arr)
    sum_of_heights = sum(distinct_heights)
    count_of_heights = len(distinct_heights)
    result = sum_of_heights / count_of_heights
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)