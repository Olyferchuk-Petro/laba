users = {                                                   # dict
    "pedro": {"password": "123", "grades": [10, 11, 8, 4, 3, 12, 5]},
    "sashak": {"password": "456", "grades": [3, 2, 4, 7, 8, 1, 4]},
    "lemyr": {"password": "789", "grades": [12, 11, 10, 9, 12, 11]},
    "rabchuk": {"password": "000", "grades": [2, 5, 6, 8, 3, 4, 10]}
}

login = input("Введіть логін: ")                            # str
password = input("Введіть пароль: ")                        # str

if login in users and users[login]["password"] == password: # bool
    grades = users[login]["grades"]                         # list
    
    print("Вхід успішний!")
    print("Всі виставлені оцінки:", grades)
    
    zadovilno = 0                                           # int
    nezadovilno = 0                                         # int
    
    for grade in grades:                                    # int
        if grade >= 5 and grade <= 12:                      # bool
            zadovilno = zadovilno + 1                       # int
        elif grade >= 1 and grade <= 4:                     # bool
            nezadovilno = nezadovilno + 1                   # int

    print("Кількість оцінок від 5 до 12 (задовільно):", zadovilno)
    print("Кількість оцінок від 1 до 4 (незадовільно):", nezadovilno)
else:
    print("Невірний логін або пароль.")
    
