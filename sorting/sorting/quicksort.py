def quicksort(arr,left,right):
    if left<right:
        paivort=partition(arr,left,right)
        quicksort(arr,left,paivort-1)
        quicksort(arr,paivort+1,right)

def partition(arr,left,right):
    i=left
    j=right-1
    pivort=arr[right]
    while i<j:
        while i<right and arr[i]<pivort:
            i+=1
        while j>left and arr[j]>pivort:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    if arr[i]>pivort:
        arr[i],arr[right]=arr[right],arr[i]
    return i




test_arr=[80,40,50,20,100,10,90,60,30,70]
quicksort(test_arr,0,len(test_arr)-1)
print(test_arr)