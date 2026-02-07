def ask_name():
    return input("Как тебя зовут? (или exit для выхода): ")

def ask_age():
    while True:
        try:
            age = int(input("Возраст: "))
        except ValueError:
            print("Ошибка ввода")
        else:
            if age <= 0:
                print("Возраст не может быть отрицательным")
            else:
                return age


def ask_role():
    while True:
        role = input("Введите роль (user/admin): ").strip().lower()

        if role in ("user", "admin"):
            return role
        else:
            print("Роль должна быть user или admin. ")

def check_access(age, role):
    # Администраторы младше 18 лет получают полный доступ независимо от возраста
    if role == "admin" and age <= 18:
        return "Полный доступ (администратор)"

    # Определение доступа по возрасту для пользователей и взрослых администраторов
    if age <= 7:
        return "Доступ ограничен (ребенок)"
    elif age <= 18:
        return "Ограниченный доступ (подросток)"
    elif age <= 60:
        return "Доступ разрешен (взрослый)"
    else:
        return "Доступ разрешен (пенсионер)"

#--------------- ГЛАВНЫЙ ЦИКЛ---------------
while True:
    name = ask_name()
    if name.lower() == "exit":
        print("Программа завершена. ")
        break

    age = ask_age()
    role = ask_role()

    access = check_access(age, role)

    print(f"\n{name}, {age} лет, роль: {role}")
    print(access)
    print("-" * 40)






