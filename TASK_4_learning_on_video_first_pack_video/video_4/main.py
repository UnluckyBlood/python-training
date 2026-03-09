number = 5 #int
str_num = "5" #str
digit = -4.5342562662 #float
word = "Результат: " #string

ril = True #bool
print (float(str_num))
print (word + str(int(str_num)+number)) #str + str(int+int)
print (number + digit) #int + float = float
print (type(number + digit))
print(word, str(ril))
print(word, ril)
print(word, number)
del number

number = 7
print("Результат: ", number)                      