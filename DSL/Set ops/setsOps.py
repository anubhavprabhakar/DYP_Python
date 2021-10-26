# python program to operate on list of sets
# intersection of sets, union of sets
# remove/avoid duplicate entries in sets

# function to remove duplicate entries from lists
def remdup(x):  # list is passed as parameter
    X=[]    # empty list that will not have duplicate entries

    for i in x:
        if i not in X:
            X.append(i)

    return X    # returns the new list, without duplicate entries


l=[1,2,3,4,5,6,7,8,9,10]    # list of students

print("List of students playing Cricket, Badminton, Football: \n", remdup(l))

C=[1,2,6,6,7] # cricket
B=[3,4,6,6,8] # badminton
F=[6,7,8,9] # football
print("\nCricket: ", remdup(C))
print("Badminton: ", remdup(B))
print("Football: ", remdup(F))


# list of students playing cricket and badminton
def intersect(C,B):
    cab=[i for i in C if i in B] #taking the intersection of A,B

    CAB=remdup(cab) # to remove duplicate entries

    print("List of students playing cricket and badminton: ",CAB)


# list of students playing either cricket or badminton but not both
def cabbnb(C,B):
    ecob=[i for i in C+B if i not in C or i not in B]  # taking intersection and then subtracting from A and B

    ECOB=remdup(ecob)   # to remove duplicate entries
            
    print("List of students playing either cricket or badminton, not both: ",ECOB)


# number of students playing neither cricket nor badminton
def ncnb(C,B):
    cbx=[i for i in range (1,len(l)+1) if i not in C and i not in B]

    CBX=remdup(cbx) # to remove duplicate entries
            
    print("Number of students playing neither cricket nor badminton: ",len(CBX))


# number of students playing cricket and football but not badminton
def cfbnb(C,B,F):
    nb=[j for j in C if j in F if j not in B]

    NB=remdup(nb)   # to remove duplicate entries
            
    print("Number of students playing cricket and football, but not badminton: ",len(NB))


# menu driven
print("\nChoose from the menu to display,\nList of students playing:\n 1. both cricket and badminton\n 2. Either cricket or badminton\n 3. neither cricket nor badminton\n 4. cricket and football but not badminton\n 0. to exit\n")
ch=int(input("Enter your choice: "))
while(ch):
    if ch==1:
        intersect(C,B)
    elif ch==2:
        cabbnb(C,B)
    elif ch==3:
        ncnb(C,B)
    elif ch==4:
        cfbnb(C,B,F)
    else:
        print("Please choose correctly.")

    ch=int(input("\nEnter your choice: "))
