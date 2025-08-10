'''Question1: Student Grades Processing
You need to write a Python program to process a student's grades. The program needs to perform the following functions:

Store information and notes for 10 students using a dictionary. Let each student have their name, surname and grades (Midterm, Final and Oral grades). For example:

image

1-Calculate each student's GPA and add it to the dictionary.

2-Find the student with the highest GPA and print it on the screen.

3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.

4-Sort the names in alphabetical order and print the sorted list on the screen.

5-Keep students with a GPA below 70 in a cluster (set).'''


from operator import length_hint
from tkinter import SEPARATOR


dic_students = { 'Ahmet Yilmaz'  : [ 85, 90, 78], #Midterm, Final, Oral
                 'Mehmet Demir'  : [ 92, 88, 76],
                 'Ayse Kaya'     : [ 78, 89, 95],
                 'Zeynep Celik'  : [ 65, 70, 80],
                 'Ali Kara'      : [ 50, 60, 55],
                 'Fatma Yildiz'  : [ 88, 85, 90],
                 'Murat Aydin'   : [ 72, 68, 74],
                 'Elif Aksoy'    : [ 95, 90, 88],
                 'Hakan Ozturk'  : [ 45, 50, 55],
                 'Canan Tas'     : [ 80, 75, 82]
            }
dic_students_1= dic_students



#1-Calculate each student's GPA and add it to the dictionary.#HAKAM

def gpa ( a , b , c  ):
    return ( ( a + b + c )/3)
gpa_max = 0
name = ""
gpa_3 =1
keep_70 = []
pos_1=0

len_dic = len (dic_students)    #print (len_dic) #10
names = list ( dic_students)     #print (names) #['Ahmet Yilmaz', 'Mehmet Demir', 'Ayse Kaya', 'Zeynep Celik', 'Ali Kara', 'Fatma Yildiz', 'Murat Aydin', 'Elif Aksoy', 'Hakan Ozturk', 'Canan Tas']
names_1 = names
values = list ( dic_students.values())
values_1 = values               #print (values) #[[85, 90, 78], [92, 88, 76], [78, 89, 95], [65, 70, 80], [50, 60, 55], [88, 85, 90], [72, 68, 74], [95, 90, 88], [45, 50, 55], [80, 75, 82]]
items = list ( dic_students.items())
items_1 = items                 #print (items) #[('Ahmet Yilmaz', [85, 90, 78]), ('Mehmet Demir', [92, 88, 76]), ('Ayse Kaya', [78, 89, 95]), ('Zeynep Celik', [65, 70, 80]), ('Ali Kara', [50, 60, 55]), ('Fatma Yildiz', [88, 85, 90]), ('Murat Aydin', [72, 68, 74]), ('Elif Aksoy', [95, 90, 88]), ('Hakan Ozturk', [45, 50, 55]), ('Canan Tas', [80, 75, 82])]
len_list= len ( items)          #print (len_list) #10
for x in range (len_dic) :      #print (values_1[x])
    gpa_1= values[x ]           #print (  gpa_1[x]   )
    Midterm = int ( gpa_1 [0]  )
    Final   = int ( gpa_1 [1]  )
    Oral    = int ( gpa_1 [2]  ) 
    gpa_2   = gpa ( Midterm, Final, Oral ) 

    if gpa_2 >= 70 :
        #print ("gpa_2= ", gpa_2 , "name = ", names[x])
        keep_70.insert (pos_1,  names [x] )
        #print ("keep_70 = ", keep_70)
        pos_1 += 1
        #print ("pos_1 =  ", pos_1 )

    if gpa_2 > gpa_max:
        gpa_max = gpa_2
        name = names [ x ]
    elif gpa_2 == gpa_max :
        gpa_3 +=1
        print (" gpa_max, gpa_2, gpa_3 " , gpa_max, gpa_2, gpa_3)
    values_1[x].append (gpa_2)                    # print ( "gpa_2 =  ", gpa_2, "\n " , values_1 )  #gpa_2 =   84.33333333333333  \n   [[85, 90, 78, 84.33333333333333], [92, 88, 76], [78, 89, 95], [65, 70, 80], [50, 60, 55], [88, 85, 90], [72, 68, 74], [95, 90, 88], [45, 50, 55], [80, 75, 82]]
    dic_students_1 [ names [x] ] = values_1[x]     # print ("x = ", x, "\n" , dic_students_1  )  # x =  0   \n  {'Ahmet Yilmaz': [85, 90, 78, 84.33333333333333], 'Mehmet Demir': [92, 88, 76], 'Ayse Kaya': [78, 89, 95], 'Zeynep Celik': [65, 70, 80], 'Ali Kara': [50, 60, 55], 'Fatma Yildiz': [88, 85, 90], 'Murat Aydin': [72, 68, 74], 'Elif Aksoy': [95, 90, 88], 'Hakan Ozturk': [45, 50, 55], 'Canan Tas': [80, 75, 82]}
print ("dic_students_1 =  " , dic_students_1  ) 
'''  dic_students_1 =   {
                            'Ahmet Yilmaz' : [85, 90, 78, 84.33333333333333],
                            'Mehmet Demir' : [92, 88, 76, 85.33333333333333],
                            'Ayse Kaya'    : [78, 89, 95, 87.33333333333333], 
                            'Zeynep Celik' : [65, 70, 80, 71.66666666666667], 
                            'Ali Kara'     : [50, 60, 55, 55.0], 
                            'Fatma Yildiz' : [88, 85, 90, 87.66666666666667], 
                            'Murat Aydin'  : [72, 68, 74, 71.33333333333333], 
                            'Elif Aksoy'   : [95, 90, 88, 91.0], 
                            'Hakan Ozturk' : [45, 50, 55, 50.0], 
                            'Canan Tas'    : [80, 75, 82, 79.0]} '''

#2-Find the student with the highest GPA and print it on the screen.

print ("\n\n\n\ngpa_max =  " , gpa_max , "with " ,name )
if gpa_3 != 1:
    print ("gpa_3 = ", gpa_3)


#3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.
#Variable:
separat_surnames  = names
separat_lastnames = names 

for c in range (0, len_list) :
   #print ( names [c])
   String_surnames_1  = String_lastnames_1 = names_1 [c] = str (names[c])
   #print ( String_surnames_1, String_lastnames_1)
   pos = String_surnames_1.find (" ")

   String_surnames_2  = String_surnames_1  [ 0     : pos ]
   String_lastnames_2 = String_lastnames_1 [ pos+1 :     ]
   #print ("sur= ", String_surnames_2, "last = ", String_lastnames_2)
  # print ("c= ", c, " pos = ", pos)###############################################

   separat_surnames [ c ]  = String_surnames_2
  # print ("the new list with surname is  :   "  , separat_surnames    )
   #print ("the new list with lastname is :   "  , separat_lastnames   )

   separat_lastnames[ c ]  = String_lastnames_2###################################################
  # print ("the new list with surname is  :   "  , separat_surnames    )
  # print ("the new list with lastname is :   "  , separat_lastnames   )

print ("the new list with surname is  :   "  , separat_surnames    )
#print ("the new list with lastname is :   "  , separat_lastnames   )

  


#4-Sort the names in alphabetical order and print the sorted list on the screen.
separat_surnames.sort()
print ( "separat_surnames   : " , separat_surnames )
separat_lastnames.sort()
print ( "separat_lastnames  : " , separat_lastnames)



#5-Keep students with a GPA below 70 in a cluster (set).

print ("keep_70 = " , keep_70)
keep_70_set = set ( keep_70)
print ( "set= ", keep_70_set )

