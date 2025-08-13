#Question 2: Take a number input from the user and write 
#a Python program that prints even numbers up to this number on the screen. 
#Do this first with 'for' and then with 'while' loops.


x = int ( input (" inter a number:  "   )  )




for n in range (0,x+1,2):
    print (n)
print (".....................................")


v=0
while v <= x :
    if v % 2 == 0:
       print (v)
       v+=2
else:
    print ( ".........................................")


