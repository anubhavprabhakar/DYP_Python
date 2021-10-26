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

arr=[2,3,4,10,11]   # already sorted array
print("List: ", arr)
x=1
print("Key: ", x)

result=binarySearch(arr,0,len(arr)-1,x)
print(result)

if result != -1:
    print("Element is present at index: ", str(result))
else:
    print("Element is not present in array.")
