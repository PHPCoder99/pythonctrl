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

    def to_csv_fmrt(self):
        return f"{self.title},{self.desc},{datetime.date.strftime(self.due_date, '%Y/%m/%d')}\n"

    def to_json_fmrt(self):
        return "{" + f'"title": "{self.title}", "desc": "{self.desc}", "due_date": "{datetime.date.strftime(self.due_date, "%Y/%m/%d")}"' + "}"

    @staticmethod
    def parse_csv(arr):
        return Note(arr[0], arr[1], datetime.datetime.strptime(arr[2], "%Y/%m/%d"))

    def __str__(self):
        return f"Записка {self.id} с именем {self.title} и описанием {self.desc}, в последний раз изменина в {datetime.date.strftime(self.date, '%Y/%m/%d')}, которую нужно выполнить к {datetime.date.strftime(self.due_date, '%Y/%m/%d')}"
