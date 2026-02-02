age = int(input("Сколько тебе лет? "))
weekend = input("Выходной? (да/нет) ") #да или нет

if 18 <= age < 60 and weekend == "Нет":
    print("Взрослый и работает")

elif 18 <= age < 60 and weekend == "Да":
        print("Отдыхаем")

else:
     print("Отдыхаем или Школа")
