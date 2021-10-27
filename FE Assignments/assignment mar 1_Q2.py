#display the average of 5 numbers using list
L=[]    #making a list
L.append(float(input("Enter first number: ")))  #taking input
L.append(float(input("Enter second number: "))) #   "   "
L.append(float(input("Enter third number: ")))  #   "   "
L.append(float(input("Enter fourth number: "))) #   "   "
L.append(float(input("Enter fifth number: ")))  #   "   "

avg=(L[0]+L[1]+L[2]+L[3]+L[4])/5    #calculating average

print("Average of the 5 numbers is= ", avg) #displaying the average
