name = input("What is your name? ")
age2 = input(f"How old are you {name}? ")
try:
    age2 = int(age2)
    print(f"{name}, you were born in {2024-age2}")
except ValueError:
    print("Please enter a valid value for your age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("You can not divide by 0!")
except:
    print("This is another type of error")

