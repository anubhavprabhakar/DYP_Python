#later, do this for 5 people
def check():
    x=int(input("Enter the age: "))
    if(x>=18):
        return "You are eligible for voting"
    else:
        return "You are NOT eligible for voting"

name=input("Enter name: ")
print(check())
