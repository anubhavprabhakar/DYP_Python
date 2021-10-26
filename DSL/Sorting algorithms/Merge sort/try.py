# merge function
def merge(arr, low, mid, high):

    n1=mid-low+1
    n2=high-mid

    # creating temp lists
    L=[0]*(n1)
    R=[0]*(n2)

    # copying data into temp lists
    for i in range(n1):
        L[i]=arr[low+i]
    for i in range(n2):
        R[i]=arr[mid+1+i]
    
    
    print(L,"   ",R)

    
    i=j=0   # initialising counters for both subarrays
    k=low     # initialising counter for merger array

    # merging two subarrays till one reaches its end
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    # copying rest of the elements from L[] subarray
    # if there is any
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
        
    # copying rest of the elements from R[] subarray
    # if there is any
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1


# merge sort
def mergeSort(arr, low, high):
    if low<high:
        mid= (low+high)//2
        print("mid: ", mid)
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)

        merge(arr, low, mid, high)


arr=[9,20,1,4,5,10,0]
print("Unsorted list: ", arr)

mergeSort(arr, 0, len(arr)-1)
print("Sorted list: ", arr)
