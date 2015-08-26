x = int(raw_input("Enter an integer"))
if (x%2 == 0):
    print("")
    if (x%3 == 0):
        print("")
        print("Div by 2 and 3")
    else:
        print("")
        print("Div by 2 and not by 3")
elif (x%3 == 0) :
    print("");
    print("Div by 3 not by 2")
