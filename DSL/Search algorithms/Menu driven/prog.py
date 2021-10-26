# bubble sort algorithm


# to swap two elements in list
def swap(arr, j):
    temp=arr[j+1]
    arr[j+1]=arr[j]
    arr[j]=temp


# bubble sort function, to be used to sort list for binary search
def bubbleSort(arr):
    n = len(arr)
    
    for i in range (n-1):   # since iteration runs n-1 times
        for j in range ((n-1)-i):   # since after every iteration,
                                    # largest element is placed at bottom,
                                    # so we need to decrease the last position by 1 every loop

            if (arr[j]>arr[j+1]):   # if next element is smaller, swap it with current element
                swap(arr, j)


# binary search with recursion
def binarySearch(arr,low,high,key):
    
    mid= (low+high) // 2
    
    if low<=high:
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binarySearch(arr,mid+1,high,key)
        elif arr[mid] > key:
            return binarySearch(arr,low,mid-1,key)
    else:
        return -1



# linear search algorithm
def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    else:
        return -1



# taking list elements from user:
n=int(input("Enter no. of elements you wish in list: "))
arr=[]
for i in range(n):
    print("Enter element ",end="")
    print(i+1,": ", end="")
    num=int(input())
    arr.append(num)

arr1=arr.copy()
bubbleSort(arr1)

print("Please select from the menu:")
print("1. Binary Search")
print("2. Linear Search")
print("0. Exit")

ch=int(input("Enter your choice : "))

while(ch):
    if ch==1:
        print("List: ", arr)
        print("For binary sort, list needs to be sorted.")
        print("Sorted list: ", arr1)
        x=int(input("Enter key to find: "))

        result=binarySearch(arr1,0,len(arr1)-1,x)
        print(result)

        if result != -1:
            print("Element is present at index: ", str(result), "in sorted list.")
        else:
            print("Element is not present in array.")

    elif ch==2:
        print("List: ", arr)
        x=int(input("Enter key to find: "))
        
        res=linearSearch(arr, x)

        if res!=-1:
            print("Element is found at index: ", str(res))
        else:
            print("Element not found in list.")

    elif ch>2 or ch<0:
        print("Please enter correct choice and try again")
        continue

    ch=int(input("Enter your choice : "))
