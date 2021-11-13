def add_two(a,b):
    return a+b

print( add_two(2,9) )

total=add_two(9,8)
print(total)

print( add_two("rohan","preet"))


def fibonacci_seq(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a,b ,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b ,end=" ")

fibonacci_seq(7)