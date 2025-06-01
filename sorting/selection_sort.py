a = [4, 8, 2, 1, 3, 7, 5]

n = len(a) - 1

for i in range(n):
    min = i
    for j in range(i + 1, n + 1):
        if a[min] > a[j]:
            min = j
    if min != i:
        a[min], a[i] = a[i], a[min]
print("Sorted array :", a)