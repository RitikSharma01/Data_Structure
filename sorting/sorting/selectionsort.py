# this is my code for selection sort
''' 
def selection_sort(arr): 
    size=len(arr)
    for i in range(size):
        min=arr[i]
        for j in range(size):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

element=[[5,2,7,9,39,8,57,1],[],[1,2,3,4,5],[10,9,8,7,6]]
for i  in element:
    print(selection_sort(i))
'''
# this is more optimised code here 


def selection_sort(arr):
    size=len(arr)

    for i in range(size-1):
        min=i
        for j in range(min+1,size):
            if arr[j]<arr[min]:
                min=j
        if i !=min:
            arr[i],arr[min]=arr[min],arr[i]
test=[[5,2,7,9,39,8,57,1],[],[1,2,3,4,5],[10,9,8,7,6]]
for element in test:
    selection_sort(element)
    print(element)
