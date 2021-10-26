
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
    i=low
    mid=(low+high)//2
    pivot=arr[mid]     # taking pivot as last element

    for j in range(low,high):
        if arr[j]<pivot:
            swap(arr, i, j)
            i+=1

    

    print("in pi:",arr)

    return i+1

arr=[5,4,0,10,2,14]
print(arr)
sort(arr,0,len(arr))
print(arr)
