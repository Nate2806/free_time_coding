import random
userinput=(input("Welcome to the Number Guesser Game! \n Pick a level: \n Level 1: 0-10 \n Level 2: 0-50 \n Level 3: 0-100"))

if userinput in ("Level 3","LEVEL 3","level 3","3","three","Three"):
    print("Level 3 has been seleceted \n Loading...")
    randomnumber=random.randint(0,100)
    while True:
        try:
            usernumber=int(input("Enter a number 1-100"))
            if usernumber == randomnumber:
                print("You guessed the number right!")
            else:
                if usernumber>randomnumber:
                    print("The number is wrong!\n The number was lower!")
                elif usernumber<randomnumber:
                    print("The number is wrong!\n The number was higher!")
        except ValueError:     
            print("PLEASE ENTER A VALID NUMBER!")
elif userinput in ("Level 2","LEVEL 2","level 2","2","two","Two"):
    print("Level 2 has been seleceted \n Loading...")
    randomnumber=random.randint(0,50)
    while True:
        try:
            usernumber=int(input("Enter a number 1-50"))
            if usernumber == randomnumber:
                print("You guessed the number right!")
            else:
                if usernumber>randomnumber:
                    print("The number is wrong!\n The number was lower!")
                elif usernumber<randomnumber:
                    print("The number is wrong!\n The number was higher!")                
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!")
elif userinput in ("Level 1","LEVEL 1","level 1","1","one","One"):
    print("Level 1 has been seleceted \nLoading...")
    randomnumber=random.randint(0,10)
    while True:    
        try:
            usernumber=int(input("Enter a number 1-10"))
            if usernumber == randomnumber:
                print("You guesses the number right!")
            else:
                if usernumber>randomnumber:
                    print("The number is wrong!\n The number was lower!")
                elif usernumber<randomnumber:
                     print("The number is wrong! The number was higher!")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!")
else:
    print("Invalid input!")
