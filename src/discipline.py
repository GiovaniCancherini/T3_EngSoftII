class Discipline:
    def __init__(self, code, name, schedule, class_number):
        self.code = code
        self.name = name
        self.schedule = schedule
        self.class_number = class_number

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_schedule(self):
        return self.schedule

    def set_schedule(self, schedule):
        self.schedule = schedule

    def get_class_number(self):
        return self.class_number

    def set_class_number(self, class_number):
        self.class_number = class_number
