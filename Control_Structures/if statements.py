if True:
    print(True)
    print("Statements")
    print("Delimited by whitespace")

num = 12

if num > 5:
    print("num is greater than 5")
    if num < 30:
        print("num is less than 30 and greater than 5")
else:
    print("num is less than 5")

if num > 5:
    print(num)
elif num < 10:      #elif is short for else if
    print("-" + num)
