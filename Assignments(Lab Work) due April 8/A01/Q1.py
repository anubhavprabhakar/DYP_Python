#Assignment 01
basicPay = int(input("Enter basic salary: "))
#showing percentage in 0.xx format, for smooth float conversion
H_R_A = 0.1*basicPay
T_A = 0.05*basicPay
totalSalary = basicPay + H_R_A + T_A
proTax = 0.02*totalSalary

#net salary is total salary minus the taxes
netSalary = totalSalary - proTax

#final output
print("Net salary payable to the employee: ", netSalary)

#waiting on user to exit
input("\nPress Enter key to exit")
