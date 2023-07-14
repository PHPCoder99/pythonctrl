import datetime


class Note:
    _id = 0

    def __init__(self, title, desc, due_date):
        self.id = self.__class__._id
        self.__class__._id += 1
        self.title = title
        self.desc = desc
        self.date = datetime.datetime.now()
        self.due_date = due_date

    def __str__(self):
        return f"Записка {self.id} с именем {self.title} и описанием {self.desc}, в последний раз изменина в {datetime.date.strftime(self.date, '%Y/%m/%d')}, которую нужно выполнить к {datetime.date.strftime(self.due_date, '%Y/%m/%d')}"
