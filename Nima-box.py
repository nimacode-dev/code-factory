import random
def rpcGame():
    print("rock-paper-scissor V1.3 is runing...\n\n")
    user = 0
    sys = 0
    while True:
        print("""
    1) rock
    2) paper
    3) scissor
    4) exit
        """)
        userChoice = input("please enter a number : ")
        print("\n")
        sysChoice = random.randint(1, 3)
        if userChoice == "1" and sysChoice == 1:
            print("system choice : rock")
            print("you'r choice : rock")
            print(f"{user} - {sys}")
        elif userChoice == "1" and sysChoice == 2:
            sys += 1
            print("system choice : paper")
            print("you'r choice : rock")
            print(f"{user} - {sys}")
        elif userChoice == "1" and sysChoice == 3:
            user += 1
            print("system choice : scissor")
            print("you'r choice : rock")
            print(f"{user} - {sys}")
        elif userChoice == "2" and sysChoice == 1:
            user += 1
            print("system choice : rock")
            print("you'r choice : paper")
            print(f"{user} - {sys}")
        elif userChoice == "2" and sysChoice == 2:
            print("system choice : paper")
            print("you'r choice : paper")
            print(f"{user} - {sys}")
        elif userChoice == "2" and sysChoice == 3:
            sys += 1
            print("system choice : scissor")
            print("you'r choice : paper")
            print(f"{user} - {sys}")
        elif userChoice == "3" and sysChoice == 1:
            sys += 1
            print("system choice : rock")
            print("you'r choice : scissor")
            print(f"{user} - {sys}")
        elif userChoice == "3" and sysChoice == 2:
            user += 1
            print("system choice : paper")
            print("you'r choice : scissor")
            print(f"{user} - {sys}")
        elif userChoice == "3" and sysChoice == 3:
            print("system choice : scissor")
            print("you'r choice : scissor")
            print(f"{user} - {sys}")
        elif userChoice == "4":
            break
        else:
            print("Invalid Choice")
            print("going to Nima box")
            break
        if user > sys:
            print("Won")
        elif user < sys:
            print("Los")
        else:
            print("Equal")
        print(f"You'r Rate : {user}\nSystem's Rate : {sys}")
      
def dice():
    print("dice V1.1 is runing...\n\n")
    while(True):
        dice = random.randint(1,6)
        print(f"dice : {dice}")
        print("""
                1) again
                2) exit
        """)
        choiceDice = int(input("please enter a number : "))
        if choiceDice == 2:
            break
        elif choiceDice == 1:
            print("\n\nnew dice created\n")
        else :
            print("you must enter 1 or 2")
            print("going to Nima box")
            break
def calculate():
    print("calculator V1.2 is runing...\n")
    while(True):
        num1 = int(input("Enter a number : "))
        num2 = int(input("Enter another number : "))
        operation = input("""
Enter a operator :
+ for addition
- for subtraction
* for multiplication
/ for division

    """)
        print("")
        if operation == '+':
            number = num1 + num2
            print(f"{num1} + {num2} = {number}")
        elif operation == '-':
            number = num1 - num2
            print(f"{num1} - {num2} = {number}")
        elif operation == '*':
            number = num1 * num2
            print(f"{num1} * {num2} = {number}")
        elif operation == '/':
            number = num1 / num2
            print(f"{num1} / {num2} = {number}")
        else:
            print("\ninvalid input")
            print("going to Nima box")
            break
        print("""
                1) again
                2) exit
        """)
        choiceCal = int(input("please enter a number : "))
        if choiceCal == 2:
            break
        elif choiceCal == 1:
            print("\n\nfield of calculator is ready\n")
        else :
            print("you must enter 1 or 2")
            print("going to Nima box")
            break



def nimaBox():
    while(True):
        print("""
        \n\nNima box (v1.8) runing...

        options :
        1) calculator
        2) dice
        3) game (rock-paper-scissor) 
        4) Exit
        """)
        choice = int(input("please enter a number : "))
        if choice == 1:
            print("""
        \ncalculator information : 

        you must enter two numbers and one operator
        than claculator will calculate your input
        and print a result

        options :
        1) start calculator
        2) Exit
        """)
            choice1 = int(input("please enter a number : "))
            if choice1 == 1:
                try:
                    calculate()
                except :
                    print("\njust enter a number")
                    print("going to Nima box")
            elif choice1 == 2:
                continue
            else:
                print("\ninvalid input")
                print("going to Nima box")
                print("go to calculator agian")
                print("and enter a number again (enter 1 or 2)")
                continue
        elif choice == 2:
            print("""
            \ndice information :

        when you start a dice
        dice will find a number between 1 to 6
        and show a number for resualt
            
        options :
        1) start dice
        2) Exit
            """)
            choice2 = int(input("please enter a number : "))
            if choice2 == 1:
                try:
                    dice()
                except:
                    print("\njust enter a number")
                    print("going to Nima box")
            elif choice1 == 2:
                continue
            else:
                print("\ninvalid input")
                print("going to Nima box")
                print("go to dice agian")
                print("and enter a number again (enter 1 or 2)")
        elif choice == 3:
            try:
                rpcGame()
            except:
                print("\njust enter a number")
                print("going to Nima box")
        elif choice == 4:
            break
        else :
            print("\ninvalid input")
            print("going to Nima box")
            print("enter a number between 1 to 3")    

try : 
    nimaBox()
except :
    print("\n\n\n\n\nprogram Nima box closed")
    print("becuse of you'r mistake")
    print("JUST ENTER A NUMBERRRRRRRRRRRRRRRRRRR!!!!!!!!!!!!!!!!!")