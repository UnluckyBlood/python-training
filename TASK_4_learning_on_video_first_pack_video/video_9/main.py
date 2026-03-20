#Кортежи меньше чем списки весят не изменяемые 
# data = (4, 6, 7, 8, 9, 21, True, 5.6, 'Hello')
# print(data[1:5]) # При выводе кортежа выводятся круглые скобки
#####data[0] = 5 #turple не имеет возможно переприсвоить элемент

# print(data.count(6))
# print(len(data)) #в кортеже работает ток две доп функции

# print (data)

#######кортеж можно создавать и без скобок
# data = 5, 7, True
# print(type(data))
# data = 5,
# print(type(data))

data = (4, 6, 7, 8, 9, 21, True, 5.6, 'Hello')

#### len не прокает
# for i in data:
    # print (i)

###### Список в кортеж
nums = [5, 7, 54]
new_data = tuple(nums)
# print(type(new_data))
word = tuple('hello world')
print (word)