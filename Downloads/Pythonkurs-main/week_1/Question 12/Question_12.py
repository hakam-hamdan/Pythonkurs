#Question 12: Get Midterm and Final grades from a student for any course. 
#The sum of 40% of the midterm exam grade 
#and 60% of the final grade will give the year-end average. 
#If the average is below 50, "FAILED" will appear on the screen, 
#and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. 
#This printing process is 4 lessons. 
#and the lessons will be written one after the other.


the_midterm_exam= 60
the_final_grade =50

average = (the_midterm_exam * 40 /100) + (the_final_grade * 60 /100)
print ( average)
if average<0 or average>100: print ( " error")
elif average>=50 : print ("SUCCESSFUL")
else : print ( "FAILED")

