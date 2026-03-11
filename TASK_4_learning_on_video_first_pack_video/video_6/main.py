#for i in range(1, 6, 2):
#    print(i)
# word = "Hello world"
# for i in word:
#     print(i * 3)

# word = "Hello world"
# count = 0
# for i in word:
#     if i == "l":
#         count += 1
# print("Count: ", count)

# for in всегда, перебор поэтому in

# i = 5
# while i < 15:
#     print(i)
#     i += 2

# isHasCar = True

# while isHasCar:
#     if input("Введи Stop: ") == "Stop":
#         isHasCar = False


# for i in range(1, 11):
#     if i == 5:
#         break    #Дроп
#     if i % 2 == 0:
#         continue #Пропуск итерации
#     print(i)

found = None
for i in "Hello":
    if i == "l":
        found = True
        break
else:
    found = False

print(found)