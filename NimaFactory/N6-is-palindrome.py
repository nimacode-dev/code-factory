def is_palindrome():
    a = input("enter a word : ").lower()
    b = a[::-1]
    if a == b :
        print(f"{a} is palindrome !")
    else:
        print(f"{a} is not palindrome !")

print("N6-is-palindrome V1.0 running...\n")
print("enter a word and see what is that")
print("is it palindrome or not\n")
is_palindrome()
