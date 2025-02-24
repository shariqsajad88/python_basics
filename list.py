a = [1, 2, 3, 30 , 4, 'gtc' ,5, 6, 7, 8, 9, 10]
print(a[0:3])
print(a[2:5])
print(a[4:7])
print(a[6:10])
print(a[1:10:2])
print(a[::2])
print(a[::-1])
print(a[::-2])
print(a[2:5][::-1]) 

a[2] = 99
print(a)
b = list(map(lambda x: 99 if x == 30 else x, a))
print(b)
print(a)
print(a[2:5][::-1]) 