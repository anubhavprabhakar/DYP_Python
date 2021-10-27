#accepting string from the user
str1=input("Enter a string: ")
newString=""

#calculating length of string
LofStr1=len(str1)
print("Length of the string is:", LofStr1)

#string reversal
for i in range(1, LofStr1+1):
    newString+=str1[-i]

print("\nReversed string:", newString)

#comparing two strings
str2=input("\nEnter another string to compare both: ")
if(str1==str2):
    print("Both strings are same/equal")
else:
    print("Both strings are different/unequal")

#checking palindrome
print("\nYour first string was:\n>>", str1, end=" <<\n")
if(str1==newString):
    print("\nIt is a palindrome")
else:
    print("\nIt is NOT a palindrome")

#checking substring
subString=input("\nEnter a substring(to be checked) to first string: ")
check=str1.find(subString, 0, LofStr1)
if(check>=0):
    print("Substring found at index", check, "of the string")
else:
    print("Substring not found")

#waiting on user to exit
input("\n\nPress Enter key to exit")
