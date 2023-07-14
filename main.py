import datetime
import os.path
import note

choice = -1

notes = []


def input_year(prompt=""):
    print(prompt)
    year = int(input("Введите год: "))
    if year < 0:
        print("Неверный год. По умолчанию текущий.")
        year = datetime.datetime.today().year
    month = int(input("Введите месяц: "))
    if month < 1 or month > 12:
        print("Неверный месяц. По умолчанию текущий.")
        month = datetime.datetime.today().month
    day = int(input("Введите день: "))
    leap_year = True
    if day < 1 or day > 31 or ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30) or (
            (month == 2 and not leap_year and day > 28) or (month == 2 and day > 29 and leap_year)):
        print("Неверный день. По умолчанию сегодняшний.")
        day = datetime.datetime.today().day
    return datetime.date(year, month, day)


def enter_notes_id(arr):
    note_id = int(input("Введите идентификатов записки, которую хотите отредактировать: "))
    while note_id < 0 or note_id >= len(arr):
        note_id = int(input("Невалидный идентификатов, попробуйте еще раз: "))
    return note_id


def enter_yn():
    yesno = input()
    while yesno.lower() != "y" and yesno.lower() != "n":
        yesno = input("Невернный ввод. Попробуйте еще раз. (y/n)")
    return yesno


def save_to_file(filename, filetype):
    pass


def import_from_file(filename, filetype):
    pass


def print_all_notes():
    pass


def find_note(date):
    pass


def add_note(title, desc, due_date):
    new_note = note.Note(title, desc, due_date)
    notes.append(new_note)
    return new_note


def edit_note(note_id, title, desc, due_date):
    delete_note(note_id)
    add_note(title, desc, due_date)


def delete_note(note_id):
    notes.pop(note_id)


saved_changes = False
while choice != 7:
    print("Введите номер комманды:")
    print("0 - сохранить изменения в файл")
    print("1 - импортировать записки из файла")
    print("2 - вывести все записки")
    print("3 - найти записку по сроку выподнения")
    print("4 - добавить записку")
    print("5 - изменить записку")
    print("6 - удалить записку")
    print("7 - выйти")

    choice = int(input())
    if choice == 0:
        filename = input("Введите имя файла: ")
        filetype = input("Введите расширение файла (csv или json): ")
        if filetype != "csv" and filetype != "json":
            print("Неверный формат файла. По умолчанию, csv.")
            filetype = "csv"
        save_to_file(filename, filetype)
        saved_changes = True
    elif choice == 1:
        filename = input("Введите имя файла: ")
        filetype = input("Введите расширение файла (csv или json): ")
        if filetype != "csv" and filetype != "json":
            print("Неверный формат файла. Проверим оба формата, но по умолчанию, csv.")
            filetype = "na"
        import_from_file(filename, filetype)
        saved_changes = False
    elif choice == 2:
        print_all_notes()
    elif choice == 3:
        find_note(input_year())
    elif choice == 4:
        add_note(input("Введите название: "), input("Введите описание: "), input_year("Введите срок выполнения: "))
        saved_changes = False
    elif choice == 5:
        print_all_notes()
        note_id = enter_notes_id(notes)
        editing_note = notes[note_id]
        field = -1
        while field != 3:
            print("Введите номер поля: ")
            print("0 - Имя")
            print("1 - Описание")
            print("2 - Срок выполнения")
            print("3 - Выйти")
            field = int(input())
            if field == 0:
                edit_note(note_id, input("Введите новое имя: "), editing_note.desc, editing_note.due_date)
                note_id = -1
            elif field == 1:
                edit_note(note_id, editing_note.title, input("Введите новое описание: "), editing_note.due_date)
                note_id = -1
            elif field == 2:
                edit_note(note_id, editing_note.title, editing_note.desc, input_year("Введите новый срок выполнения: "))
                note_id = -1
            elif field == 3:
                break
        saved_changes = False
    elif choice == 6:
        print_all_notes()
        note_id = enter_notes_id(notes)
        print("Вы точно хотите удалить эту записку? (y/n)")
        print(notes[note_id])
        yesno = enter_yn()
        if yesno == "y":
            delete_note(note_id)
            saved_changes = False
    elif choice == 7:
        if not saved_changes:
            print("Вы не сохранили изменения. Вы точно хотите выйти? (y/n)")
            yesno = enter_yn()
            if yesno == "y":
                break
        else:
            break
