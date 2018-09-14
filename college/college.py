class Human:
    def __init__(self, first_name, last_name, patronymic='', data_birth=None, gender=None, ):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.data_birth = data_birth
        self.gender = gender

    def __str__(self):
        if self.patronymic[0]:
            return f'человек: {self.first_name} {self.last_name[0]}. {self.patronymic[0]}.'
        else:
            return f'человек: {self.first_name} {self.last_name[0]}.'

    @classmethod
    def import_from_file(cls, file_name):
        items_source = open(file_name, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for items_dict in items_source_as_dict:
            _items = cls(**items_dict)
            items.append(_items)

        return items


class Student(Human):
    def __init__(self, first_name, last_name, height, wight, *args, **kwargs):
        super().__init__(first_name, last_name, *args, **kwargs)
        self.height = height
        self.wight = wight

    def set_group(self, group):
        self.group = group

    def __str__(self):
        if self.patronymic[0]:
            return f'Студент: {self.last_name}  {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f'Студент: {self.last_name} {self.first_name[0]}.'


class Group:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f'Группа {self.name} ({self.specialty.split()[-1]})'

    def add_students(self, students):
        for student in students:
            student.set_group(self)


class Teacher(Human):
    def __init__(self, first_name, last_name, education, experience, *args, **kwargs):
        super().__init__(first_name, last_name, *args, **kwargs)
        self.education = education
        self.experience = experience

    def __str__(self):
        if self.patronymic:
            return f'Учитель ({self.education}): {self.last_name}  {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f'Учитель ({self.education}): {self.last_name} {self.first_name[0]}.'


