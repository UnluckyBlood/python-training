print("hello")
# Проверка через какой файл запущенно, так как мы вызываем этот модуль, то вызов у нас идёт с modules.py и он ней является main файлом для файла, мэйном считается только если мы сделаем вызов от сюда
if __name__ == "__main__":
    print("hello_модуль")

def hi():
    print("Hello world!")
def add(x,y):
    try:
        return x+y
    except (ValueError, TypeError):
        return("Передайте числа")

