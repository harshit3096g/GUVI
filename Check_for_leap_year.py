a=raw_input("Enter any year...\n")
a=int(a)
if a%4==0:
    print "This ia a leap year"
elif a%4!=0:
    print "This ia not a leap year"
else:
    print "Try again"