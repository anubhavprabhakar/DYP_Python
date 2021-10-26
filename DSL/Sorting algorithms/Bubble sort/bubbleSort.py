# bubble sort algorithm


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



arr=[]  # initialising empty array

n=int(input("Enter the number of elements you want to enter: "))

# taking list elements from user
for i in range(n):
      print("Enter element",i+1,end="")
      print(": ", end="")
      num=int(input())
      arr.append(num)

print("Unsorted: ", arr)
bubbleSort(arr)
print("Sorted: ", arr)
