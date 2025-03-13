#searching using loop
arr = [1,2,3,4,5,6,7,8,45,34,655]
target = 777
i = 0
n = len(arr)
isPresent = False

while i <= n-1:
    if arr[i] == target:
        isPresent= True
        break
    i += 1
if isPresent == True:
    print("Number found")
else:
    print("number not found")