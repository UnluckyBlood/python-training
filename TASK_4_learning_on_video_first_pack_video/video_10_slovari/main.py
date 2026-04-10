# списки []    list
# кортежи ()   tuple
# Словарь {}   dist
# country = []
# country = ()
# country = {}
# print (type(country))

country = {4: 3}
print (country[4])

country = {True: 3}
print (country[True])

# работает по сути как case можно внутри прописать кортеж
country = {(5, 6): 3}
print (country[(5, 6)])

# можно удобно обращаться по ключу, а не индексу
country = {'code': 'RU','name': 'Russia', 'population': 144}
print (country['name'])

# можно через dict, но фигурной удобнее
# country = dict(code='RU', name='Russian')
# print (country['name'])

print (country)

# перебор циклом ключей
for key in country:
    print (key)

print(country.items())
# перебор циклом значений
for key, value in country.items():
    print (value)

for key, value in country.items():
    print (key, " - ", value)


# метод get аналагичен [] скобкам
print(country.get('name'))

# полная очистка нашего словаря
# country.clear()

# Удалить элемент
# country.pop('name')
# удалить последний элемент
# country.popitem()
# получить ключи или значения или всё
print(country.keys())
print(country.values())
print(country.items())

# Для обновления данных
# country.update()
# или есть проще
country['code'] = 'None'
print(country['code'])

#Словарь внутрь словаря и как с этим работать
person = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Marley',
        'age': 45,
        'address': ['г. Ярославль', "ул. Нефтяников", "32145"],
        'grades': {'math': 5, 'physics': 3}
    },
    'user_2':{
        'first_name': 'Neitan',
        'last_name': 'Marley',
        'age': 45,
        'address': ['г. Ярославль', "ул. Нефтяников", "32145"],
        'grades': {'math': 5, 'physics': 3}
    }
}

print (person['user_1']['address'][1])