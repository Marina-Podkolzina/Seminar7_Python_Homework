import csv

def search(name, phone):
    with open("book.csv", encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter = "|")
        count = 0
       
        for row in reader:
            if row['Имя'] == name:
                print (f'Номер телефона контакта - {row["Телефон"]}', end='')
            elif row['Телефон'] == phone:
                print (f'Имя контакта - {row["Имя"]}', end='')
        
            count += 1
        print()


        
def add(name, phone):
    
    with open("book.csv",mode='a', encoding='utf-8') as f:
        names = ["Имя", "Телефон"]
        writer = csv.DictWriter(f,  delimiter="|", lineterminator="\r", fieldnames=names)
        
        writer.writerow({"Имя": f'{name}', "Телефон": f'{phone}'})
    print ("Контакт успешно добавлен")
    
    print ("Список всех контактов:")
    with open("book.csv",mode='r', encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter="|")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'{" - ".join(row)}')
            else:
                print(f'{row[0]} - {row[1]}')
            count += 1
    print()
    print (f'Всего {count-1} контактов в записной книге')    

def print_contact():
    with open("book.csv",mode='r', encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter="|")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'{" - ".join(row)}')
            else:
                print(f'{row[0]} - {row[1]}')
            count += 1
    print (f'Всего {count-1} контактов в записной книге')