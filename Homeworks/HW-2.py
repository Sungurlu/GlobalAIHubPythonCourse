d1 = {"Name" : "Bahar" , "GPA" : "3,82" , "Birth year" : "1999" , "University" : "ITU" , "Job" : "Mechanial Engineer"}
d2 = {"Name" : "Zehra", "GPA" : "3,04" , "Birth year" : "1964" , "University" : "KTU" , "Job" : "Mechanial Engineer"}
d3 = {"Name" : "Ayşe" , "GPA" : "3.5" , "Birth year" : "1973" , "University" : "Gazi" , "Job" : "Dentist"}
d4 = {"Name" : "Hakan" , "GPA" : "2,98" , "Birth year" : "1994" , "University" : "KTU" , "Job" : "Civl Engineer"}
d5 = {"Name" : "Adem" , "GPA" : "3,21" , "Birth year" : "1992" , "University" : "Selçuk" , "Job" : "Lawyer"}


a=[d1.values(),d2.values(),d3.values(),d4.values(),d5.values()]

for i,j,k,l,m in a:
    print(i,", ",j," ortalamaya sahip",k,"doğumlu,",l,"'de/da",m, "bölümünde okumakta")