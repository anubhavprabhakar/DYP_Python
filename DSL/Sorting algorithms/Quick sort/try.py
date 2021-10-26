
# swap
def swap(arr, i, j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

# quick sort
def sort(arr, low, high):
    if low<high:
        pi=partition(arr, low, high)

        sort(arr, low, pi-1)
        sort(arr, pi+1, high)


# partition
def partition(arr, low, high):
    i=low-1
    pivot=arr[high]     # taking pivot as last element

    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            swap(arr, i, j)

    swap(arr, i+1, -1)

    return i+1

arr=[5,4,0,29,10,2]
print(arr)
sort(arr,0,len(arr)-1)
print(arr)
