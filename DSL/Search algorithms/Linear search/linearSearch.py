# linear search algorithm

def search(arr, key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    else:
        return -1

arr=[2, 3, 1, 5, 9, 10]
print("List: ", arr)

# possible case 1
x=5
print("Key: ", x)

res=search(arr, x)

if res!=-1:
    print("Element is found at index: ", str(res))
else:
    print("Element not found in list.")

# possible case 2
x=12
print("Key: ", x)

res=search(arr, x)

if res!=-1:
    print("Element is found at index: ", str(res))
else:
    print("Element not found in list.")
