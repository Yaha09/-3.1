# На вход получаем строку, состоящую из двух чисел и символа между ними. На выходе получаем результат операции с числами.
# Операция определяется символом:

#  # - возвращает остаток от деления второго числа на первое
# ! - возвращает число, у которого сумма цифр больше
# @ - возвращает большее число из двух
# $ - возвращает число, у которого больше цифр
# В случае если оба числа удовлетворяют условию, то возвращается первое.

# Примеры:
# 28#26379 => 3
# 1111!23 => 23
# 123@876 => 876
# 456$0007 => 0007


xх = 0
while True :

    data_entry = input("""       # - возвращает остаток от деления второго числа на первое
       ! - возвращает число, у которого сумма цифр больше
       @ - возвращает большее число из двух
       $ - возвращает число, у которого больше цифр
    введите число1 "#" "!" "@" "$" число2 :""") 

    if data_entry.find("#") >= 0 :
        team = data_entry.find("#")
        number1 = data_entry[:team]
        number2 = data_entry[team+1:]
        print("остаток от деления второго числа ",int(number2) % int(number1))


    if data_entry.find("!") >= 0 :
        team = data_entry.find("!")
        number1 = data_entry[:team]
        number2 = data_entry[team+1:]
        a ,b = 0 ,0
        for x in number1:
            a = a + int(x)
        for x in number2:
            b = b + int(x)
        if a < b:
            print("большая сумма цифр у числа2 ",number2)
        else:
            print("большая сумма цифр у числа1 ",number1)


    if data_entry.find("@") >= 0 :
        team = data_entry.find("@")
        number1 = data_entry[:team]
        number2 = data_entry[team+1:]
        x = len(number1)
        y = len(number2)
        if x < y :
            print("Большее число ",number2)
        else:
            print("Большее число ",number1)


    if data_entry.find("$") >= 0 :
        team = data_entry.find("$")
        number1 = data_entry[:team]
        number2 = data_entry[team+1:]
        x = len(number1)
        y = len(number2)
        if x < y :
            print("Большее цифр у числа2 ",number2)
        else:
            print("Большее цифр у числа1 ",number1)

    xx = input ('введите "n" для выхода :')
    if xx == "n":    
        break








