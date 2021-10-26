# Quick Sort algorithm


# function to swap two elements in the array
def swap(arr, i, j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

# main function implementing quick sort
def quickSort(arr, low, high):
    if low<high:
        pi=partition(arr, low, high)    # to sort around pivot

        quickSort(arr, low, pi-1)   # sort the left side of pivot
        quickSort(arr, pi+1, high)  # sort the right side of pivot


# seperating elements smaller and greater than pivot
def partition(arr, low, high):

    pivot=arr[high] # taking last element as pivot

    i=low-1     # setting index for smaller number

    for j in range(low, high):
        if arr[j]<pivot:    # if current element is less than pivot, then swapping arr[i] with current element,
                            # else we ignore i and arr[]
            i+=1
            swap(arr, i, j)
    swap(arr, i+1, high)    # now swapping high with last position of i+1
    return (i+1)

arr=[]
n=int(input("Enter no. of elements you wish to enter: "))

for k in range(n):
    print("Enter element ", end="")
    print(k+1,": ", end="")
    num=int(input())
    arr.append(num)

    
print("Unsorted: ", arr)

quickSort(arr, 0, len(arr)-1)
print("Sorted: ", arr)
