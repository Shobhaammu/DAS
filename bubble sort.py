def bubble_sort(l):
    n=len(l)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                
my_list=[64,34,25,12,22,11,90]
print('original list: ',my_list)
bubble_sort(my_list)
print('sorted list: ',my_list)