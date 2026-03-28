import time
# подключать модули через запятую можно, но плохой тон так как уменьшает читабельность кода
import math
# можем указывать с помощью as *псевдоним* краткий вызов
import datetime as d
import random as r
# С помощью os можно добавлять инфу про пк
import os

#  если не уверены что модуль есть то можно использовать try
try:
    import nomodule
except ImportError:
    print("Модуль nomodule не найден!!!")

#  называть модули новые не зарезервированными именнами и не цифрами, а кратким что в нём есть
#  Если в модуле написать что-то не вызываемыми функциями, а просто действиями сразу, то при импорте они воспроизведутся , например щас написали внутри print
import module

print (r.random())
print (os.getcwd())
print(math.e)
time.sleep(3)
print("Hello")

print(d.datetime.now().time().hour)
rs = "dwa"
print(module.add(rs,2))
print(module.add(2,5))



# так же можно импортировать только определённую функцию из модуля 
from module import hi
# и тогда мы можем к этой функции обращаться напрямую, будто она находится в этом же файле
# из модуля можем их много добавлять закрыв в скобки и через запятую from module import (hi, add, ...)
hi ()
# можем с помощью as назвать их как нам удобно
from module import hi as h, add as a
h()
print(a(25,15))