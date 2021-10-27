#for calculating square root
def squareRoot(num):
    root = num**(1/2)
    return root

#for calculating square
def square(num):
    sq = num**2
    return sq

#for calculating cube
def cube(num):
    cu = num**3
    return cu

#for checking for prime
def prime(num):

    #for counting the number of factors

    n=0   #to store the number of factors  
    
    for i in range(1, num+1):
        if(num%i==0):
            n+=1
        if(n>2):    #if number of factors is more than 2
            break

    #loop will pass to here is the number is a prime number
    if(n==2):
        return "is a prime number."
    else:
        return "is NOT a prime number."

#for calculating factorial of a number
def fac(num):
    #initializing variable to store products
    factorial=1

    for i in range(1, num+1):
        factorial*=i

    return factorial


n=int(input("Enter a number: "))

print("\n\t Square root of", n, "is", squareRoot(n))
print("\n\t Square of", n, "is", square(n))
print("\n\t Cube of", n, "is", cube(n))
print("\n\t", n, prime(n))
print("\n\t Factorial of", n, "is", fac(n))

#waiting on user to exit
input("\n\nPress Enter key to exit")
