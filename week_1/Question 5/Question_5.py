#Question 5: Write a Python program that takes a positive integer input 
#from the user and calculates its factorial. 
#Factorial is the product of all positive integers between a number itself and 1. 
#For example: if the user entered 5, the program should give the following output: 
#Enter a number from the user: 5 Factorial: 120



number = int ( input ( " enter a positive number:  "))
v = 1
if number <0 :
    print ( number , " is negative")

else :
    for x in range ( 1, number + 1 ):
        v = v * x 
    print ( number , "factorial : " , v)

