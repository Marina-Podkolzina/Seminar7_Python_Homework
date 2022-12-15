n = 0
name = ''
phone = ''
def talk():
    print("Что вы хотите сделать?")
    print("Найти контакт - 0")
    print("Добавить новый контакт - 1")
    print("Просмотреть список всех контактов - 2")
    print("Введите соответствующее число")
    global n
    n = int(input())
    global phone
    global name
    if n == 0:
        print("Введите имя, если известно:")
        name = str(input())
        print("Введите номер телефона, если известно:")
        phone = str(input())
        print()
    elif n == 1:
        print("Введите имя:")
        name = str(input())
        print("Введите номер телефона:")
        phone = str(input())
        print()
    elif n != 2:
        print("Некорректный ввод!")
        
        return talk()

