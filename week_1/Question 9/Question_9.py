
#Question 9: How to create a combination of loop and conditional statement 
#that takes a word input from the user 
#and checks whether that word is a palindrome 
#(the same when read backwards)?


word = "12345654321"

l=len(word)
print (word)
ok=0
for x in range (0,l):
   # print (x)
   # print ( "word x  ", word[x])
    #print ( "word l-1-x " , word[l-1-x])
    if word[x] == word [l-x-1]:
        ok+=1
        #print ( "word x  ", word[x])
        #print ( "word l-1-x " , word[l-1-x])
   # print (ok)
if ok ==l:
    print ( "ok")
else:
   (print ("not ok" ))
