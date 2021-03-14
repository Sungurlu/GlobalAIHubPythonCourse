

S1=input("Student-1 Name:")
print("------",S1,"------")
i1=int(input("Student-1, please enter your Midterm: "))
j1=int(input("Student-1, please enter your Project: "))
k1=int(input("Student-1, please enter your Final: "))

S2=input("Student-2 Name:")
print("------",S2,"------")
i2=int(input("Student-2, please enter your Midterm: "))
j2=int(input("Student-2, please enter your Project: "))
k2=int(input("Student-2, please enter your Final: "))

S3=input("Student-3 Name:")
print("------",S3,"------")
i3=int(input("Student-3, please enter your Midterm: "))
j3=int(input("Student-3, please enter your Project: "))
k3=int(input("Student-3, please enter your Final: "))

S4=input("Student-4 Name:")
print("------",S4,"------")
i4=int(input("Student-4, please enter your Midterm: "))
j4=int(input("Student-4, please enter your Project: "))
k4=int(input("Student-4, please enter your Final: "))

S5=input("Student-5 Name:")
print("------",S5,"------")
i5=int(input("Student-5, please enter your Midterm: "))
j5=int(input("Student-5, please enter your Project: "))
k5=int(input("Student-5, please enter your Final: "))

passing_grade_1=((i1)*(3/10)+(j1)*(3/10)+(k1)*(4/10))
passing_grade_2=((i2)*(3/10)+(j2)*(3/10)+(k2)*(4/10))
passing_grade_3=((i3)*(3/10)+(j3)*(3/10)+(k3)*(4/10))
passing_grade_4=((i4)*(3/10)+(j4)*(3/10)+(k4)*(4/10))
passing_grade_5=((i5)*(3/10)+(j5)*(3/10)+(k5)*(4/10))

d1={S1 : passing_grade_1 , 
    S2 : passing_grade_2 ,
    S3 : passing_grade_3 , 
    S4 : passing_grade_4 ,
    S5 : passing_grade_5 }

list = [(k, v) for k, v in d1.items()] 
new_student_list=sorted(list,reverse=True)
print(new_student_list)