def max_input():
    a = int(input("enter a first number : "))
    b = int(input("enter a second number : "))
    c = int(input("enter a third number : "))
    max = a # a = b = c ==> max = (a or b or c)
    if a > b and a > c:
        max = a
    if b > a and b > c:
        max = b
    if c > a and c > b:
        max = c
    print(f"max number is {max}")


print("N3-max-input V1.0 running...\n")
print("enter three numbers and take a max number")
max_input()
