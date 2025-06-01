a = [5, 0, 1, 5, 8]
n = int(input("Element to be searched : "))
flag = 0
for i in range(len(a)):
    if a[i] == n:
        flag = 1
        print("Element found at index",i)
if flag == 0:
    print("Not Found")