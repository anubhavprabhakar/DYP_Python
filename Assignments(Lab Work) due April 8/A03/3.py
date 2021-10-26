#list to hold value of marks
marks=[]

#for checking whether marks in each course is equal and above 40, or not
check=True  #becomes false if any course has marks less than 40

print("Enter marks for each course out of 100")

#accepting marks of 5 courses
for i in range(1,6):
    print("Marks for course",i,": ", end="")
    marks.append(int(input()))
    if(marks[i-1]<40):
        check=False

#calculating and printing aggregate
agg=sum(marks)/5
print("\nYour aggregate is: ", agg)

#printing result
if(check==False):
    print("\nYou failed.\nYou did not score more than 40 in one or more courses.")
    
else:
    print("\nYou passed with ", end="")
    if(agg>=75):
        print("distinction!")
    elif(75>agg>=60):
        print("first division!")
    elif(60>agg>=50):
        print("second division!")
    else:
        print("third division!")

#wait on user to exit
input("\n\nPress Enter key to exit")
