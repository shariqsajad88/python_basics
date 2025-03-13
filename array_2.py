grocery = [10]
arr = [20,30,40]
print(grocery)

grocery.append("brinjal")
print(grocery)
grocery.append("onion")
print(grocery)
grocery.append("apple")
print(grocery)
grocery.insert(2,"milk")
print(grocery)
print(grocery[1:5:2])#slicing
print(grocery.pop(2))
print(10 in grocery)
grocery.remove(10)
print(grocery)
print(10 in grocery)
grocery.append(arr)
print(grocery)
grocery.extend(arr)
print(grocery)