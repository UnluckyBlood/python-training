# наследование, класс наследник наследует методы, поля, конструкторы

class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, "| City:", self.city)

# допустим придётся множество функций в этот класс например штук 30, это не очень удобно, поэтому мы можем создавать дочерние классы которые будут принимать все характеристики верхнего класса
# и при этом в другом классе мы пропишем функции чтоб не было нагромождения
class Shop(Building):
    pass # если оставим чисто pass, то все функции переданы в этот класс и мы можем вызывать все теже методы
class School(Building):
    # или например указывание переменных которые логичны только для определенного здания, тут  ученики
    pupils = 0
    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city) # Передача данных  в класс конструктор, super вызывает супер класс(класс родитель) указать наш класс через который вызываем и параметр self
        # дальше обращаемся к конструктору и какие данные передаём , чтобы передать в род класс
        # Без супера не передадутся данные в род класс
        self.pupils = pupils
# в пайтоне нельзя указать несколько родительских классов в С++ можно было, у наследника может быть ещё один наследник, например так
class House(School):
    pass
# полиморфизм, мы можем переписывать методы что объявленены в родителях, можем переписывать в наследниках
class Medical(Building):
    pacient = 0
    
    def __init__(self,pacient, year, city):
        super(Medical, self).__init__(year, city)
        self.pacient = pacient
# таким образом мы заменяем выбираемый метод на более дочерний, иначе мы можем обратиться именно к родительному в коде вызова
# мы могли просто прописать так же как в род, но легче через супер
    def get_info(self):
        super().get_info()
        print("Pacient:", self.pacient)

# инкапсуляция это по сути защита данных, что доступ к данным должен быть через конструкции, доступ всегда есть в пайтоне, но именно сам вывод не будет работать
# производится она с помощью двух нижних подчеркиваний перед переменной, пример
class frfrfr:
    __chirik = None
    def __init__(self, chirik):
        self.chirik = chirik
    def get_info(self):
        print("Chiriki:", self.chirik)    
class dochfrfr(frfrfr):
    fr = 0
    def __init__(self,fr, chirik):
        super(dochfrfr, self).__init__(chirik)
        self.fr = fr

school = Building(2000, 'Moscow')
house = Building(2000, 'Moscow')
# Работает даже без функций внутри class Shop
shop = Shop(2000, 'Moscow')
shop.get_info()

school = School(100,2002,'Vorkuta')
school.get_info()


medical = Medical(13500, 1986, "Yaroslave")
medical.get_info()


# инкапсуляция выводы
inc1 = frfrfr(1523)
print(inc1.chirik)
# print(inc1.__chirik)
inc2 = dochfrfr(123,324523235)
print(inc2.chirik,inc2.fr)
# print(inc2.__chirik)