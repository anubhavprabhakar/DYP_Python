# binary search without recursion

def binary_search(arr,key):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if arr[mid] < key:
            low=mid+1
        elif arr[mid] > key:
            high=mid-1
        else:
            return mid
    return -1

arr=[2,3,4,10,40]
print("List: ", arr)

# possible case 1
x=10
print("Key: ", x)

result=binary_search(arr,x)

if result !=-1:
    print("Element is present at index: ", str(result))
else:

    print("Element is not present in array.")

# possible case 2
x=18
print("Key: ", x)

result=binary_search(arr,x)

if result !=-1:
    print("Element is present at index: ", str(result))
else:

    print("Element is not present in array.")
