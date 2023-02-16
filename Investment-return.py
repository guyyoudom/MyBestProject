# This lab will calculate the investment return after 10, 20, and 30 years of investment
#Display the Initial message
print("If I start with $1000 and invest it at 7% return for the")
print("following amounts of time, I can expect to end up with...")
#Initializing principale p
p=1000
#Initializing annual rate r
r=7
#looping for the number of year 10,20,30
n=10,20,30
for n in range(10,31,10):
    #Input the amount on deposit at the end of the nth years
    a=p*(1+r/100)**n
    #Display the amount
    print("Amount after {} years: ${:.2f}".format(n,a))
