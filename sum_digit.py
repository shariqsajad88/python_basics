def sum(lst):
    ans = 0
    for i in range(len(lst)):
        ans = ans + lst[i]
        print(ans)


lst = [1,2,3,4,5]
sum(lst)