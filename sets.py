st = set("6")
st.add(15)
st.add(10)
st.add(20)
st.add(15)
st.add(6)
print(st)
print(8 in st)
st.remove(6)
print(st)

lis = [1,2,2,2,2,3,3,3,3,4,4,4,4]
print(list(set(lis))) #typeconversion