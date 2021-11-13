name="Rachana"

#string indexing
print(name[2]) #will print c that is alphabet at second index from beginning.
print(name[-2]) # will print n that is second index alphabet from end.

#string slicing
print(name[1:5]) #will print 'acha' as 5th alphabet will not be included.
print(name[0:-2])
print(name[0:]) #Rachana will be printed
print(name[:]) #Rachana will be printed
print(name[4:])
print(name[:-3])

print(name[0:5:2]) #will print skipping 2 letters in between

print(name[0:4:-1]) # will reverse the string


# USER INPUT
age=input("Enter your age:")
print(age)

u_name, u_age = input("Enter your name and age:").split()
print("Name:", u_name)
print("Age:", u_age)

gender , phone = input("Enter your gender and phone number:").split(",")
print("Gender:", gender)
print("Phone number:", phone)

print(len(u_name)) #will print the length of u_name variable                                                                                                                                                                                              
