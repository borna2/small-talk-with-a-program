name = input("Whats your name: ")
age = input("How old are you: ")
location = input("What country do you live in: ")
print("Hey " + name + "! You are " + age + " years old.")
print("Is it nice in " + location + "?(yes or no): ")
x = input()
if x == "yes" or x == "Yes" or x == "YES":
    print("cool!")
elif x == "no" or x == "No" or x == "NO" or x == "nO":
    print("Oh okay.")
else:
    print("it was a yes or no question. Try again.")
    x1 = input()
    if x1 == "yes" or x1 == "Yes":
        print("Awesome!")
    elif x1 == "no" or x1 == "No" or x1 == "NO" x1 == "nO":
        print("Oh okay.")
    else:
        print("thats not a yes or no response!")
