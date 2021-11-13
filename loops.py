i=1
while i<5:
    print("This is line",i)
    i+=1

for i in range(1,11,2):
    print (i)
print("\n")
for i in range(1,15,2):
    if i==5:
        continue
    if i==11:
        break
    print (i)

for i in "Rachana":
    print(i)

    