a = [4, 8, 2, 1, 3, 7, 5]
for i in range (1, len(a)):
    item = a[i]
    j = i-1
    while j >= 0 and a[j] > item:
        a[j+1] = a[j]
        j-=1
    a[j+1] = item
print(a)