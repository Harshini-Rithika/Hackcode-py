distinct_stamps = set()
N = int(input())
for _ in range(N):
    country_name = input()
    distinct_stamps.add(country_name)
print(len(distinct_stamps))
