
drinks = ["whiskey", "rum", "tequila", "gin", "sake", "wine", "beer", "vodka"]
mixers = ["fanta", "fanta limon", "red bull", "tonic", "cola", "soda"]

#print(f"{choice(drinks)} {choice(mixer)}")
#print("I am the virtual bartender, welcome to my humble bar")
name = input("How should I call you?")

try:
    age = input("How old are you")
    age = int(age)
    legal = None
    country = input("What country are you from")
    if age < 14:
        legal = False
        print("You are too young to be here")
    elif age < 16:
        if country == "Austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "Austria" or country == "Luxembourg":
            legal = True
        else:
            legal = True
    elif age < 21:
        if country == "USA" or country == "UAE":
            legal = False
        else:
            legal = True
    else :
            legal = True


except ValueError:
    print("I don't have time for your games! Get out!")
