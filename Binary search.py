L1=[int(x) for x in input('enter the list of number separated by spaces:').split()]
key=int(input('enter the number to be search'))
start,end=0,len(L1)-1
found=False
while start<=end:
    mid=(start+end)//2
    if L1[mid]==key:
        print(f"the key {key} is found at index {mid}.")
        found=True
        break
    elif L1[mid]<key:
        start=mid+1
    else:
        end=mid-1
        
if not found:
    print(f" key {key} is not found in the list")
   
        