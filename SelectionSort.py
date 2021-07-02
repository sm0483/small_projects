arr=list(map(int,input("input the list of numbers to sort: ").split()))
def SelectionSort(): #It finds minimum value in list 
    minvalue=None
    for element in arr:
        if minvalue is None or minvalue>element:
            minvalue=element
    return minvalue
ls=[] #The new list to save sorted element
for _ in range(len(arr)):
    ls.append(SelectionSort())
    arr.remove(SelectionSort())
print(ls)    
