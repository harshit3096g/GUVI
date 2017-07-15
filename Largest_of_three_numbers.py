a=raw_input("Enter 1st number...\n")
b=raw_input("Enter 2st number...\n")
c=raw_input("Enter 3st number...\n")
a=int(a)
b=int(b)
c=int(c)
if (a>b) and (a>c):
    largest = a
elif (b>a) and (b>c):
    largest = b
else:
    largest =c
print "The largest amongst the numbers entered is " + str(largest)