def valid_zip_cod():
    z = input("enter a zip code : ")
    int(z)  # if not only number ==> error
    if len(z) > 5 or len(z) < 5:
        print("invalid zip code")
    else:
        print("valid zip code")


print("N5-valid-zip-code V1.0 running...\n")
print("valid zip code only has 5 number\n")
valid_zip_cod()
