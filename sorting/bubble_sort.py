a = [4, 8, 2, 1, 3, 7, 5]

n = len(a) - 1

for i in range(n):
    for j in range(n - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print("Sorted array :",a)