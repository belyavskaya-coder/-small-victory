def ask_name():
    name = input("What is your name? ")
    return name


def ask_age():
    while True:
        age = int(input("What is your age? "))
        if age < 0:
            print("Error, age cannot be negative?")
        else:
            return age

name = ask_name()
age = ask_age()
print(f"Hello, {name}! You a {age} old")