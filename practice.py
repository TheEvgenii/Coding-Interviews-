arr = [0,1,2,3,4]
for i in range (len(arr)-1):
    if arr[i] == 0:
        arr[-1] == arr[i]

print(arr)