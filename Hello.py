#This program says hello and asks for name and age

print('Hello Vladim!')
print('What is your name?')#asks for name

myName=input()
print('Its good to meet you, ' +myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')#asks for age

myAge=input()
print('You will be '+str(int(myAge)+1)+' in a year.')

wait=input()
