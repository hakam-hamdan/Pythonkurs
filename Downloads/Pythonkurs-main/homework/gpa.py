students = {'Ahmet Yilmaz'  : [ 85, 90, 78], #Midterm, Final, Oral
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
for name, grades in students.items():
    midtern, final, oral=grades
    gpa=round((midtern+final+oral)/3, 2)
    students[name] = [midtern,final,oral,gpa]
print("gpa for student:") 
for name, data in students.items() :
    print(f"{name}:gpa={data[3]}")
top_students = max(students, key=lambda name: students[name][3])
print("hight gpa:")
print(f"{top_students}:gpa={students[top_students][3]}")
name_tuples = [tuple(name.split(" " , 1)) for name in students]
print(name_tuples)
stored_names = sorted(name_tuples)
print(stored_names)
low_gpa_studentes = {name for name , data in students.items()
                     if data[3] < 70}
print("gpa < 70:")
print(low_gpa_studentes)
