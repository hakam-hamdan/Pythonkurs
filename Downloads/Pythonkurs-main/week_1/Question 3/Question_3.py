#Question 3: Write a Python code that receives a start and end value from 
#the user and prints all the numbers between these values ​​
#(including the end value) on the screen.

start = int (input ( "enter ther start number")  )
end = int (input ( "enter ther end number")  )
if start>end : print ( "start > end")
else:
    for x in range ( start, end + 1):
        print ( x )