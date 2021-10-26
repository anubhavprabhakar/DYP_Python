# string operations
# displaying longest word
# frequency of a particular char
# checking for palindrome
# index of first occurance of substring
# occurance of each word


def palindrome(s1):
    rev=s1[::-1] #reverses the string and stores it in rev
    
    if(s1==rev): #comparing original string with the reversed string
        print("\'", s1, "\', is a palindrome")
    else:
        print("\'", s1, "\', : is NOT a palindrome")


def index(s1):
    print("Enter a substring: ")
    substr=input() #reading substring from user
    res=s1.find(substr,0,len(s1)) #finding substring in the main string

    if(res!=-1): #find() returns -1 if it doesnt find what it searches
        print("Index of first occurance of \'", substr, "\' is: ", res)
    else:
        print("Substring is not found.")


def freqchar(s1):
    char=input("Enter the character: ")
    f=0 #storing the frequency

    for i in range(len(s1)): #traversing through the original string, one char at a time
        if(s1[i]==char): #comparing the character in string with the char to be found
            f+=1 #increases frequency when the char is found
    print("The count of occurance of \'", char, "\' is", f)
    

def longword(s1):
    br=s1.split() #splitting the string into list of words (default seperator is blankspace)
    s2=sorted(br,key=len)   #sorting the list with the size of the words (default is ascending order)
                            #using s2, so that nothing changes in original string
    
    print("Longest word(s): ")
    
    for i in range(1,len(s2)+1):    #now checking in the list
                                    #to traverse list from last element to first
        
        if(len(s2[-i])==len(s2[-1])):   #print the biggest word
                                        #as well as check if another word is as big as the biggest word
           print(s2[-i])    #print the word

        else:
            break;  #to ignore all the words smaller than the biggest word


def occurance(s1): 
    l=[]    #to store words in a list that are already counted
    
    br=s1.split()
    verify=0     #to verify presence of already printed word
    
    for i in range(0, len(br)):     # going thru br[]
        for n in range(0, len(l)):  # for checking already printed word
            if(br[i]==l[n]):    # if word is present in l[], its already printed
                verify=1        # if word is already printed, this is proof
                break
            
        if(verify==0):   # if word is not already printed
            
            print("Occurance of \'", br[i],"\' is: ", s1.count(br[i]))
            l.append(br[i])     # add the word in list of already printed words
            
        verify=0     # reset proof of print for another use



print("Enter a string: ")
s1=input()

#menu
print("\nChoose from the menu:")
print("1. Display longest word")
print("2. Frequency of occurence of particular character")
print("3. Check if the string is palindrome or not")
print("4. Display index of first occurance of the substring")
print("5. Count occurance of each word in a string")
print("0. To exit the program")

choice=int(input("\nEnter your Choice: "))

while(choice):
    if(choice==1):
        longword(s1)
    elif(choice==2):
        freqchar(s1)
    elif(choice==3):
        palindrome(s1)
    elif(choice==4):
        index(s1)
    elif(choice==5):
        occurance(s1)
    elif(choice>5 or choice<0):
        print("Please enter correct choice and try again.")
        
    choice=int(input("\nEnter your Choice: "))

print("\n===== Thank You =====")
