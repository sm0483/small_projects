def linearSearch(inp,arr):
    for i in range(len(arr)):
        if arr[i]==inp:
            return i
    return -1   

     
        
if __name__=="__main__":
    arr=list(map(int,input("Enter the elemets in arry: ").split()))
    inp=int(input("Enter the number your are searching for: "))
    print("elemet is at "+  str(linearSearch(inp,arr)))


        
