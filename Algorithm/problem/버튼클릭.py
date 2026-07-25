arr = [5, 1, 3, 2, 4, 6]

queries = [
    (0, 2),
    (1, 4),
    (3, 5)
]

prefix = [0]

for n in arr:
    prefix.append(prefix[-1] + n)

for left, right in queries:
    print(prefix[right+1] - prefix[left])