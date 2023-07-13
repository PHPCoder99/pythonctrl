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
