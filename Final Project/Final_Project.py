print("-----WELCOME TO OUR KNOWLEDGE COMPETITION-----\n")

Total=0

starter=input("Should we start?\n")

print("Please answer YES/NO\n")

if starter=="YES":
    Q_1=print("Q_1.) What is 10+62/2 = ?")
    print("------------------------------")
    print("A-) 10")
    print("B-) 20")
    print("C-) 30")
    print("D-) 41")
    print("E-) 51\n")
    q_1=input("Your answer:  \n")

    if q_1 == "D":
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0
    
    Q_2=print("Q_2.) Which one is the capitol of Turkey?")
    print("------------------------------")
    print("A-) İstanbul")
    print("B-) Çorum")
    print("C-) Trabzon")
    print("D-) Muş")
    print("E-) Ankara\n")
    q_2=input("Your answer:  \n")
    
    if q_2 == "E" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

    Q_3=print("Q_3.) Which one is the vehicle registration plate number of Trabzon ?")
    print("------------------------------")
    print("A-) 13")
    print("B-) 35")
    print("C-) 61")
    print("D-) 06")
    print("E-) 67\n")
    q_3=input("Your answer:  \n")

    if q_3 == "C" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

    Q_4=print("Q_4.) Which one of the options below is the  name of the donkey character from the famous cartoon 'Winnie the Pooh'?  ?")
    print("------------------------------")
    print("A-) Eeyore")
    print("B-) Piglet")
    print("C-) Tiger")
    print("D-) Winnie")
    print("E-) Dumbo\n")
    q_4=input("Your answer:  \n")

    if q_4 == "A" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

    Q_5=print("Q_5.) When did Atatürk die?")
    print("------------------------------")
    print("A-) 1881")
    print("B-) 1938")
    print("C-) 1923")
    print("D-) 1950")
    print("E-) 1920\n")
    q_5=input("Your answer:  \n")

    if q_5 == "B" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

    Q_6=print("Q_6.) What is 5!= ?")
    print("------------------------------")
    print("A-) 120")
    print("B-) 24")
    print("C-) 5")
    print("D-) 25")
    print("E-) 250\n")
    q_6=input("Your answer:  \n")

    if q_6 == "A" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

    Q_7=print("Q_7.) When did Turkey become a NATO member?")
    print("------------------------------")
    print("A-) 1945")
    print("B-) 1950")
    print("C-) 1952")
    print("D-) 1950")
    print("E-) 2003\n")
    q_7=input("Your answer:  ")

    if q_7 == "D" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

    Q_8=print("Q_8.) Who is the first president of the Republic of Turkey?")
    print("------------------------------\n")
    print("PLEASE WRITE FULL NAME\n")
    q_8=input("Your answer:  \n")

    if q_8 == "Mustafa Kemal Atatürk" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

    Q_9=print("Q_9.) What is (6389+51521+64546)*0= ?")
    print("------------------------------")
    print("A-) 64546")
    print("B-) 51521")
    print("C-) 6389")
    print("D-) 122456")
    print("E-) 0\n")
    q_9=input("Your answer:  \n")

    if q_9 == "E" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

    Q_10=print("Q_10.) Which one is the capital of Italy?")
    print("------------------------------")
    print("A-) Torino")
    print("B-) Milano")
    print("C-) Napoli")
    print("D-) Rome")
    print("E-) Venice\n")
    q_10=input("Your answer:  \n")

    if q_10 == "D" :
        print("Correct!!!\n")
        Total=Total+10
    else:
        print("Wrong!!!\n")
        Total=Total+0

else :
    print("Thank you for coming. See you next time.\n")



if Total>=50:
    print("SUCCESS\n")
else:
    print("FAILED\n")
print("Total points:   ",Total)