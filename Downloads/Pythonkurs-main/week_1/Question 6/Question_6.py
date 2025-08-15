
#Question 6: Write a Python code that receives a number from the user 
#and checks whether this number is prime.

number = int ( input (" enter a number:  " )  )
#t=2
if number <=1 : print (" not prime")
else : 
    for x in range ( 2, number):
            if number %x ==0 :
                print (" not prime")
                break
            else: print ("is prime")






'''for x in range (2 , number  ):
    #print ("x= ", x ) # test 
    t+=1
    if number % x ==0 :
       t = number  + 1 
       #print ( "t = ", t )
       #print ( "x = ", x )
       print ( number ," / ", x , " = ", number/x )
#print (".............")  # for is end
if t== number:
    print ( number, " is prime ")
else : 
    print ( number , " is not prime" )'''