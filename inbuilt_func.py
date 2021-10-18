######## USEFUL IN-BUILT FUNCTIONS ########

# 1. round() function round the value to the specified number of places or to nearest integer 
print(round(3.14126))
print(round(3.14126,2))

# 2. divmod(x,y) function outputs the quotient and remainder in a tuple.
a=divmod(27,5)
print(a)     # prints both quotient and remainder
print(a[0])  # prints only quotient 
print(a[1])  # prints only remainder

# 3. isinstance() return True, if first argument is the instance of that class. Multiple classes can also be checked at once. 
print(isinstance(1,int))
print(isinstance(1.0,int))
print(isinstance(1.0,(int,float)))

# 4. pow(x,y,z) x raise to the power y and remainder by z 
print(pow(2,5,3))
print(pow(2,5))  # dsame as 2**5

# 5. input() used to take input from the user. 
e=input("Enter a number:")
print(type(e))  # whatever is inputed through input() function will have type as STRING
print("Entered number is:",e)
e=int(e)  # changed the type from STRING  to INT
print(type(e))
f=float(input("Enter float number:"))
