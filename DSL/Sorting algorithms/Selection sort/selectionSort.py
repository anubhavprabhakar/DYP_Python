# selection sort algorithm


# swap function
def swap(arr, i, j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp


# main selection sort function
def selectionSort(arr):
    for i in range(len(arr)-1): # range is len(arr)-1 since main iteration should run upto length of array minus 2 times
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                swap(arr, i, j)


arr=[10,18,9,100,40,18,2]
print("Unsorted list: ", arr)

selectionSort(arr)
print("Sorted list: ", arr)
