print("Enter details of Person 1:")
p1={'name':input('Enter name: '), 'age':int(input('Enter age: ')), 'pkg':float(input('Enter package: ')), 'loc':input('Enter location: ')}
print("\nEnter details of Person 2:")
p2={'name':input('Enter name: '), 'age':int(input('Enter age: ')), 'pkg':float(input('Enter package: ')), 'loc':input('Enter location: ')}

print("\nDetails of Person 1:\n")
print("\tName: ", p1['name'], "\n\tAge: ", p1['age'], "\n\tPackage: ", p1['pkg'], "\n\tLocation: ", p1['loc'])

print("\nDetails of Person 2:\n")
print("\tName: ", p2['name'], "\n\tAge: ", p2['age'], "\n\tPackage: ", p2['pkg'], "\n\tLocation: ", p2['loc'])

p1['loc']=input("\nEnter new location for person 1: ")
p2['loc']=input("Enter new location for person 2: ")

print("\nNew Details:")
print("Person 1:")
print("\tName: ", p1['name'], "\n\tLocation: ", p1['loc'])

print("\nPerson 2:")
print("\tName: ", p2['name'], "\n\tLocation: ", p2['loc'])
