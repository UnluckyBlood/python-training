# Урок с функциями, def, lambda

def test_func():
    pass # аналог nop
    print("Hello", end="") # end использукется для того чтобы вместо переноса строки вставить нулевой символ, чтоб следующий принт был в той же строке вывода
    print("!")

test_func()

# Передача параметров
def test_func(word):
    pass # аналог nop
    print(word, end="") # end использукется для того чтобы вместо переноса строки вставить нулевой символ, чтоб следующий принт был в той же строке вывода
    print("!")
    word = "sdf"
    print(word)

test_func("hi")
test_func(5.6)

def summa(a, b):
    print(a+b)

summa(5, 32.5)
# summa(23,"hi") # не работает так как строчку нельзя суммировать с числом

# в видосе не предлагали фикс, но загуглил нашёл проверку isinstance который пишется по правильному if isinstance(a, str) *(*название переменной, и тип данных)*
def sum_t_i(a, b):
    if a or b == isinstance(str):
        a,b=str(a),str(b)
    print(a+b)
sum_t_i("23", 123)

# возврат из функции с помощью ретёрн

def sum_t_i(a, b):
    if a or b == isinstance(str):
        a,b=str(a),str(b)
    return(a+b)
res = sum_t_i("23", 123)
print (res)
print (sum_t_i(321,"rffrf"))

nums1 = [5,7,9,4,2,15,-15]

min_number = nums1[0]

for i in nums1:
    # print (min_number)
    if i<min_number:
        min_number = i
# print (min_number)        

def mininmum(l):
    min_number = l[0]
    for i in l:
        if i < min_number:
            min_number = i
    return (min_number)
print (mininmum(nums1))

nums2 = [4.2, 4.5, 12.5, 32.5, "frfrfr", True] 
# print (mininmum(nums2)) #ошибка из-за текста
# Сделал с проверкой на текст, да значение по int будет не минимальным, но будет минимум по str для некоторых случаев
def mininmum(l): 
    min_number, i=None,None
    for el in l:
        if isinstance(el, str):
            l = [str(el) for el in l] # циклом конвертируем каждый элемент списка в строчку для проверки, так как текст не всегда возможно перевести в int или float
            break
    min_number = l[0]
    for i in l:
        if i < min_number:
            min_number = i
    return (min_number)
x = mininmum(nums2)
print (type(x) , x )
x = mininmum(nums1)
print (type(x) , x )

# альтернатива, игнорировать текст
def mininmum(l): 
    min_number = l[0]
    for i in l:
        if isinstance(i, str):
            continue        
        if i < min_number:
            min_number = i
    return (min_number)
x = mininmum(nums2)
print (type(x) , x )
y = mininmum(nums1)
print (type(y) , y )
x=[x,y]
print(mininmum(x))

# лямда функции , return сразу идёт
func = lambda x, y: x*y
print (func(5, 2))
# лямда функция для коротеньких функций, как тернарная
