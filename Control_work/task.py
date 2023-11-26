def read_csv(filename): # функция чтения файла
    note_book= []
    fields = ['Название заметки', 'Содержание заметки']

    with open(filename, 'r', encoding= 'utf-8') as nb:
        for line in nb:
            record = dict(zip(fields, line.split(',')))
            note_book.append(record)
            
    return note_book


def write_csv(filename, note_book): # фукция записи файла
    with open('notes.csv', 'w', encoding= 'utf-8') as phout:
        for i in range(len(note_book)):
            s = ''
            for v in note_book[i].values():
                s+= v +','
            phout.write(f'{s[:-1]}\n')
             

def show_menu(): # функция вывода на экран меню
    print(
        '1. Распечатать все заметки',
        '2. Найти заметку по названию',
        '3. Изменить заметку',
        '4. Удалить заметку',
        '5. Добавить новую заметку',
        '6. Закончить работу', sep = "\n")
    choice = int(input('Введите номер вызываемой команды: '))
    return choice

def work_with_notebook(): # основная фукция по работе с заметками
    choice = show_menu()
    note_book = read_csv("notes.csv")
    while choice <=5:
        if choice == 1:
            print_result(note_book)
        elif choice == 2:
            name = input('Введите название заметки: ')
            print(find_name(note_book, name))
        elif choice ==3:
            name = input('Введите название заметки: ')
            new_text = input('Введите текст: ')
            print(change_note(note_book, name, new_text))
        elif choice == 4:
            name = input('Введите название заметки: ')
            print(delete_name(note_book, name))
        elif choice == 5:
            user_data = input('Введите через запятую название заметки и текст: ')
            print(add_user(note_book, user_data))
            write_csv('notes.csv', note_book)
        
        choice = show_menu()


# функция вывода на печать
def print_result(note_book):
    for i in note_book:
        print (i)
    return 
# функция нахождения заметки по названию
def find_name(note_book, name):
    for item in note_book:
        if item['Название заметки'] == name:
            return item['Содержание заметки']
    return   
#функция замены текста заметки
def change_note(note_book, name, new_text):
    for item in note_book:
        if item['Название заметки'] == name :
            item['Содержание заметки'] = new_text
            return #item['Содержание заметки']
    return
# функция удаления заметки
def delete_name(note_book, name):
    new_note_book = []
    for item in note_book:
        if item['Название заметки'] == name:
            note_book.pop(item)
    return note_book
# функция добавления новой заметки
def add_user(note_book, user_data):
    fields = ['Название заметки', 'Содержание заметки']
    new_record = dict(zip(fields, user_data.split(',')))
    note_book.append(new_record)
    return note_book

work_with_notebook()