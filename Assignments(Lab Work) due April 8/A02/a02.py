#initialising list
nums=[]

#number of elements
N=5

print("Enter 5 numbers:")

#looping
for i in range(0, N):
    nums.append(int(input()))

#print the list
print("Your inputs are: ", nums, "\n")

#performing operations on the list
Max = max(nums)
Min = min(nums)
Sum = sum(nums)

#use sum and len to calculate average of the list
Avg = Sum/N

#displaying required data
print("\tMaximum in list: ", Max)
print("\tMinimum in list: ", Min)
print("\tSum of the elements: ", Sum)
print("\n\tAverage of the list: ", Avg)

#to wait on user to exit
input("\nPress any key to exit")
