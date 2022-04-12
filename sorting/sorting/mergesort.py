def mergesort(arr):
    if len(arr)>1:
        #divide  array
        left_arr=arr[0:len(arr)//2]
        right_arr=arr[len(arr)//2:len(arr)]

        #call mergesort recursively
        mergesort(left_arr)
        mergesort(right_arr)

        #merge the array
        i=0 #for index of left array
        j=0 # for index of right array
        k=0 #for index of merged array
        while i<len(left_arr) and j< len(right_arr):

            if  left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1

test_arr=[1,2,3,4,5,6,7,8]
mergesort(test_arr)
print(test_arr)