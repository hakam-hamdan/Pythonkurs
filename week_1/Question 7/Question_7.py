#Question 7: How to create a loop that calculates the Fibonacci sequence 
#and returns the result as a list containing numbers up to a certain limit?

number = 2
# variable:
fib_befor = 1
fib_now=1
fib_betwin=1

if number == 0:
	print ( " the Fibonacci sequence of 0 = 0 " )

if number == 1:
	print ( " the Fibonacci sequence of 1 = 1 " )

if number == 2:
	print ( " the Fibonacci sequence of 2 = 1 " )
#print ( "fib_befor = " , fib_befor , "fib_now = " , fib_now  , "fib_betwin = ", fib_befor)

if number > 2:
    for x in range (3 , number+1) :
        #print ("x= ", x )
        fib_betwin=fib_now
        fib_now += fib_befor
        fib_befor= fib_betwin
        #print ( "fib_befor = " , fib_befor , "fib_now = " , fib_now  , "fib_betwin = ", fib_befor)  
        #fib_now = fib_betwin + fib
        #print ( "fib_befor = " , fib_befor , "fib_now = " , fib_now  , "fib_betwin = ", fib_befor)            
        #print ( "......")
        #print ( "fib_befor = " , fib_befor , "fib_now = " , fib_now  , "fib_betwin = ", fib_befor)
    print ( " the Fibonacci sequence of " , number, " = ", fib_now )
