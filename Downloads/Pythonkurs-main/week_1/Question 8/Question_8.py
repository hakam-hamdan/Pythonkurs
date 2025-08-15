#Question 8: Write a Python code that takes a word from the user 
#and prints the reverse of this word on the screen.

word = input ("enter ther word:  " )
#print (word)
z = len (word)
#print (z)
revers = ("")
print (revers)

for x in range (0, z): 
    n=z-1-x
   # print ( word [n])
    l= word [n]
    #print (l)
   # print (revers )
   # revers [x] = word [n]
    revers += l
    #print (x)  
print (revers )
