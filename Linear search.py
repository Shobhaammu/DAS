L1=input('enter the list of number separated by spaces:').split()
L1=[int(x) for x in L1]
#linear search
key=int(input('enter the number to be search'))
found=False
for i in range(len(L1)):
    if L1[i]==key:
        print(f"the key {key} is found at index {i}.")
        found=True
        break
    
else:
    print(f"{key} is not found in list.")
        