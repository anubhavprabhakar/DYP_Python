#initializing empty list
List=[]
even=[]
odd=[]

print("Enter 10 numbers")

for i in range(0, 10):
    List.append(int(input()))

for i in range(0, 10):
    if(List[i]%2==0):
        even.append(List[i])
    else:
        odd.append(List[i])

print("\nEntered values: ", List)
print("\nEven List: ", even)
print("\nOdd List: ", odd)

#waiting on user to exit
input("\nPress Enter key to exit")
