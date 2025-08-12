'''
Question 2: Film Library Management System Project
Project Description: This project aims to create an application that will help the user manage their movie collection. Users can add, edit, delete movies and view their collection.

Data Structures Used: Dictionaries (to store movies and related information), lists (to display movie collection)

Basic Functions:

1-Create a movie data by taking information such as movie name, director, release year and genre from the user and store it in a dictionary.

2-Give the user the option to edit or delete a movie. (For this, a suitable function must be written for whatever data they want to change about the movie.)

3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.

4-Save the movie data in a file and restore this data when you start the program.
'''


#1-Create a movie data by taking information such as movie 
#name, 
#director, 
#release year and 
#genre from the user 
#and store it in a dictionary.



from tkinter import TRUE


list_film     = []
list_director = []
list_year     = []
list_form     = []
dic_film = {}
while_ok      =  "ok" 
for_while=0
while while_ok == "ok":
    list_film.append    (  input ( "enter the name :\n"                                  ))
    list_director.append(  input ( "enter the director :\n"                              ))
    list_year.append    (  input ( "enter the year :\n"                                  ))
    list_form.append    (  input ( "enter the form :\n"                                  ))

    dic_film_film      = { list_film [for_while]: list_film[for_while] }
    dic_film_director  = { list_film [for_while]: list_director[for_while] }
    dic_film_year      = { list_film [for_while]: list_year[for_while]     }
    dic_film_form      = { list_film [for_while]: list_form[for_while]     }

    dic_film = {"list_film"     : list_film,
                "list_director" : list_director,
                "list_year"     : list_year ,
                "list_form"     : list_form
                }

    for_while += 1
    while_ok           =  input ( "for more films enter: ok \n or enter onther:\n")
print ("dic_film =  ", dic_film)

#2-Give the user the option to edit or delete a movie. 
#(For this, a suitable function must be written for whatever data they want to change about the movie.)

while_ok = "ok"
while while_ok == "ok":
    enter = input ( "enter ther filmname that you will chang : \n")
    pol= enter in list_film 
    if  pol == True:
        index = list_film.index(enter)
        #print("the index of " , enter, "is in the list_film of index: " , index)
        edit= input ("what do you will edit? enter: \nadd\nremove\n?edit\n")
        if edit == "add":
            list_film.append    ( input ("enter the new film: \n"))
            list_director.append( input ("enter the director .\n"))
            list_year.append    ( input ("enter the year:\n"    ))
            list_form.append    ( input ("enter the form:\n"    ))
            dic_film = {"list_film"     : list_film,
                        "list_director" : list_director,
                        "list_year"     : list_year ,
                        "list_form"     : list_form
                        }
            print ("dic_film = ", dic_film)

        elif edit == "remove":
             list_film.remove    (list_film [index])
             list_director.remove(list_director [index])
             list_year.remove    (list_year [index])
             list_form.remove    (list_form [index])

             dic_film = {"list_film"     : list_film,
                         "list_director" : list_director,
                         "list_year"     : list_year ,
                         "list_form"     : list_form
                         }
             print ("dic_film = ", dic_film)

        elif edit == "edit":
             list_film[index]     = ( input ("enter the film \n"))
             list_director[index] = ( input ("enter the director \n"))
             list_year[index]     = ( input ("enter the year \n"))
             list_form[index     ]= ( input ("enter the form \n"))
             dic_film = {"list_film"     : list_film,
                       "list_director" : list_director,
                       "list_year"     : list_year ,
                      "list_form"     : list_form
                      }
             print ("dic_film = ", dic_film)
        else :
            print ("error")

    else :
      index = "the film isnot in the list"
      #print  (index)
      edit = input ( "dou you will add a new film? enter add: ")
      if edit == "add":
            list_film.append    ( input ("enter the new film"))
            list_director.append( input ("enter the director"))
            list_year.append    ( input ("enter the year"    ))
            list_form.append    ( input ("enter the form"    ))
            dic_film = {"list_film"     : list_film,
                        "list_director" : list_director,
                        "list_year"     : list_year ,
                        "list_form"     : list_form
                        }
      #print ("dic_film = ", dic_film)
    while_ok = input ("enter ok when do you will find anether film: " )


#3-Allow the user to view their collection. 
#List all movies or filter by criteria such as genre or year of release.

number_films= len(list_film)
print( "number_film : " , number_films)

while_ok="ok"
while while_ok == "ok":
    enter = input ( "enter the film name, thet you will watch:\n" )
    pol= enter in list_film

    if  pol == True:
        index = list_film.index(enter)
        #print("the index of " , enter, "is in the list_film of index: " , index)
        dic_film_name = {
                           "film"     : list_film[index], 
                           "director" : list_director[index], 
                           "year"     : list_year[index], 
                           "form"     : list_form[index]
        }
        print ("dic_fil_name = ", dic_film_name)


    else :
      print( "the film isnot in the list")
      
    while_ok = input ("enter ok when do you will watch anether film: " )


#4-Save the movie data in a file and restore this data when you start the program.

