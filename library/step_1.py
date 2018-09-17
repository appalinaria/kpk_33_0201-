from library import Author, Production

author = Author.import_from_file('author.src')
[print(el) for el in author]

print('*' * 30)
production = Production.import_from_file('production.src')
[print(el) for el in production]
