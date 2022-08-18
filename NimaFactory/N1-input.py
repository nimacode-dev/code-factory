print("N1-input V1.2.1 running...\n")
print("enter two numbers and take a addition result of them")
try:
    a = int(input("enter a first number : "))
    b = int(input("enter a second number : "))
except:
    print("you must enter an integer number")
    print("N1-input closed")
    print("run again and enter an integer number")
print("\n")
c = a + b
print(f"first number is {a} and second number is {b} so result is {c}")
print("thank you for using N1-input")
