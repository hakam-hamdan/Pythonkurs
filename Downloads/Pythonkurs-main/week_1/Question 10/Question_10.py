#Question 10: Write the code that calculates the person's 
#weight index and returns the result as underweight, 
#overweight or overweight according to the index value. 
#(You can look on the internet for the weight index calculation) 
#To do this, ask the user for their weight and height measurements. 
#weight index If it is below 25, it is weak, Between 25-30 is normal, 
#If you are over 30-40, you are overweight. If you are over 40, you are overweight.


#يتم الحساب كما يلي:
#مؤشر كتلة الجسم (BMI )= الطول بالمتر X الطول بالمتر / وزن الجسم بالكيلوغرام (يرجى قراءة المعادلة من اليسار إلى اليمين)
l=77
w=70
BMI =  ( l * l ) / w 
print (BMI)

#النحافة الشديدة
#أقل من 16

#النحافة المعتدلة
#16 - 17

#النحافة الخفيفة 
#17 - 18.5

#الوزن الطبيعي
#18.5 - 25

#زيادة الوزن
#25 - 30

#السمنة من الفئة الأولى
#30 - 35

#السمنة من الفئة الثانية
#35 - 40

#السمنة من الفئة الثالثة
#أكثر من 40

if BMI <16 : print ( " النحافة الشديدة")
elif BMI >= 16 and BMI<17 : print ( " النحافة المعتدلة") 
elif BMI >= 17 and BMI<18.5 : print ( " النحافة الخفيفة  ") 
elif BMI >= 18.5 and BMI<25 : print ( " الوزن الطبيعي ") 
elif BMI >= 25 and BMI<30 : print ( " زيادة الوزن") 
elif BMI >= 30 and BMI<35 : print ( " السمنة من الفئة الأولى") 
elif BMI >= 35 and BMI<40 : print ( "السمنة من الفئة الثانية ") 
else: print ( " السمنة من الفئة الثالثة")
