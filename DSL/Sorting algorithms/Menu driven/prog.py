


# to swap two elements in list
def swap(arr, i, j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp






# main bubble sort function
def bubbleSort(arr):
    n = len(arr)
    
    for i in range (n-1):   # since iteration runs n-1 times
        for j in range ((n-1)-i):   # since after every iteration,
                                    # largest element is placed at bottom,
                                    # so we need to decrease the last position by 1 every loop

            if (arr[j]>arr[j+1]):   # if next element is smaller, swap it with current element
                swap(arr, j, j+1)






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






# main selection sort function
def selectionSort(arr):
    for i in range(len(arr)-1):     # range is len(arr)-1 since main iteration should run upto length of array minus 2 times
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                swap(arr, i, j)






# merge sort algorithm
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
    
    
    #print(L,"   ",R)   # line(s) i used to debug merge sort

    
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


# main merge sort function
def mergeSort(arr, low, high):
    if low<high:
        mid= (low+high)//2
        #print("mid: ", mid)    # line(s) i used to debug merge sort
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)

        merge(arr, low, mid, high)










l=[]    # initialising empty array


n=int(input("Enter the number of elements you want to enter in list: "))

# taking list elements from user
for i in range(n):
      print("Enter element",i+1,end="")
      print(": ", end="")
      num=int(input())
      l.append(num)



# menu driven
print("\nMenu:")
print("1. Bubble sort")
print("2. Quick sort")
print("3. Selection sort")
print("4. Merge sort")
print("0. Exit")

ch=int(input("\nEnter your choice: "))

while(ch):
    if ch==1:
        arr=l.copy()
        print("\nUnsorted list: ", arr)
        bubbleSort(arr)
        print("Bubble sorted list: ", arr)

    elif ch==2:
        arr=l.copy()
        print("\nUnsorted list: ", arr)
        quickSort(arr, 0, len(arr)-1)
        print("Quick sorted list: ", arr)

    elif ch==3:
        arr=l.copy()
        print("\nUnsorted list: ", arr)
        selectionSort(arr)
        print("Selection sorted list: ", arr)

    elif ch==4:
        arr=l.copy()
        print("\nUnsorted list: ", arr)
        mergeSort(arr, 0, len(arr)-1)
        print("Merge sorted list: ", arr)

    elif ch>4 or ch<0:
        print("Please choose correct option.")

    ch=int(input("\nEnter your choice: "))


print("\n================ Thank You =================")
