def ask_name():
    return input("What is your name? ")

def ask_age():
    while True:
        age = int(input("What is your age? "))
        if age <= 0:
            print("Error: age must be positive")
        else:
            return age

def check_access(age):
    if age >= 18:
        return "Доступ разрешен"
    else:
        return "Доступ запрещен"

name = ask_name()
age = ask_age()
result = check_access(age)

print(f"{name}, тебе {age} лет. {result} ")
