a = [0, 1, 2, 3, 4, 5]
n = int(input("Element to be searched : "))
l = 0
flag = 0
r = len(a) - 1
while l <= r:
    m = (l + r) // 2
    if n < a[m]:
        r = m - 1
    elif n > a[m]:
        l = m + 1
    else:
        flag = 1
        break
if flag == 1:
    print("Element found at index", m)
else :
    print("Element not found")