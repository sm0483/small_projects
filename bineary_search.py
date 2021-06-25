
def BinearySearch(arr,find):
    first=0
    last=len(arr)
    while True:
        i=int((first+last)/2)
        if arr[i]<find:
            first=i
            last=len(arr)
        elif arr[i]>find:
            first=0
            last=i
        else:
            print(f"yes it is there at {i+1}")
            break
        
    

    
arr=list(map(int,input("enter the list of numbers: ").split()))
arr.sort()
find=int(input("Enter the number you want to search: "))
if __name__=="__main__":
    print(arr)
    BinearySearch(arr,find)         
         
