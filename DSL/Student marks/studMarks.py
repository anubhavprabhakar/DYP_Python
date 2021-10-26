# input marks of n students
# perform operations on the marks obtained
# use 'ab' or 'AB' for absent students

n=int(input("enter number of students in a class :"))
studMarks=[]    # list for storing marks(with 'ab')

for i in range(n):
    marks=input("Enter marks of student/'ab' for absent: ")
    if(marks!='ab' and marks!='AB'):
        studMarks.append(int(marks))
    else:
        studMarks.append('ab')  # converts 'AB' to 'ab' before storing in studMarks list
print("\nList of students is :", studMarks)    

l=[]    # new list for storing marks without 'ab', so integer operations would be easier
for m in studMarks:
        if(m!='ab'):
            l.append(m)
            
def average():
    avg=sum(l)/n
    print("the average of students marks is :",avg)

def highScore():
    highestScore=max(l)
    print("highest marks obtained are: ",highestScore)

def lowScore():
    minscore=min(l)
    print("lowest score obtained is :",minscore)

def abscount():
    print("Number of absentees is: ", studMarks.count('ab'))    # used only 'ab' since main list stored 'AB' as 'ab'

def hfreq():
    freq=1  # since all marks appearing once will not count towards highest frequency
    r=0     # to store the mark which had highest frequency

    for m in l:
        if(l.count(m)>freq):
            freq=l.count(m)
            r=m
    if(freq>1):
        print("Marks obtained by most students is: ", str(r))
    else:
        print("All marks obtained are unique")
    
    
    
choice=int(input("Menu:\n 1. Average \n 2. Highest score \n 3. Lowest score\n 4. Count of absentees\n 5. Marks with highest frequency \n 0. to exit\nPlease enter your choice to display: ")) 

while(choice):  # choice of 0 itself will terminate the loop
    if choice==1:
        average()
    elif choice==2:
        highScore()
    elif choice==3:
        lowScore()
    elif choice==4:
        abscount()
    elif choice==5:
        hfreq()

    else:
        print("invalid choice")

    choice=int(input("Please enter your choice to display: "))

print("========Thank You=========")
