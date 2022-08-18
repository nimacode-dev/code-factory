def triangle():
    print("at a first you must set a rows number")
    number_of_rows = int(input("enter number of rows : "))
    print("now you must set a character")
    print("if you enter nothing the default character will chosen")
    print("default character = * ")
    character = input("enter a character : ")
    if not character:
        character = '*'
    for i in range(number_of_rows):
        i += 1
        print(character * i)


print("N7-triangle V1.0 running...\n")
print("enter a number and a character after that take a triangle\n")
triangle()
