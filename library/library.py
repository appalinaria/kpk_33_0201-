class Library:
    def __init__(self, first_name_author, last_name_author, patronymic_author, production_name):
        self.first_name_author = first_name_author
        self.last_name_author = last_name_author
        self.patronymic_author = patronymic_author
        self.production_name = production_name

    def __str__(self):
        if self.production_name:
            return f'Автор: {self.first_name_author} {self.last_name_author[0]} {self.patronymic_author[0]},\
             произведение {self.production_name}'
        else:
            return f'Неизвестный автор, произведение {self.production_name}'

    @classmethod
    def import_from_file(cls, Library):
        items_source = open(Library, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for items_dict in items_source_as_dict:
            _items = cls(**items_dict)
            items.append(_items)

        return items


class Author(Library):
    def __init__(self, first_name_author, last_name_author, patronymic_author, date_birth, date_death):
        # super().__init__(first_name_author, last_name_author, patronymic_author, production_name)
        self.date_birth = date_birth
        self.date_death = date_death
        self.first_name_author = first_name_author
        self.last_name_author = last_name_author
        self.patronymic_author = patronymic_author
        # self.production_name = production_name

        # *args, ** kwargs

    def __str__(self):
        if self.date_birth[0]:
            return f'Автор: {self.first_name_author} {self.last_name_author} {self.patronymic_author}, годы жизни {self.date_birth} - {self.date_death}'
        else:
            return f'Автор {self.first_name_author} {self.last_name_author} {self.patronymic_author}, дата смерти {self.date_death}.'


class Production(Library):
    def __init__(self, production_name, date_written, publication_date, publication_city):
        # super().__init__(production_name)
        self.production_name = production_name
        self.date_written = date_written
        self.publication_date = publication_date
        self.publication_city = publication_city

    def __str__(self):
        if self.date_written:
            return f'Произведение {self.production_name}: написано в {self.date_written}, опубликовано {self.publication_date} в {self.publication_city}.'
        else:
            return f'Произведение {self.production_name} опубликовано {self.publication_date} в {self.publication_city}.'
