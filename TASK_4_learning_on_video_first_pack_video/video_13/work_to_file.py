# если файла нет создаётся автоматически(но не папку, папку надо создать или использовать os.makedirs(*"название папки"*, exist_ok=True)) и ей нужна библиотека import os, а так же надо всегда закрывать файлы чтоб не было утечки памяти
#второй параметр это способ открытия файла "w" - write открываем и полностью переписываем файл
file = open('TASK_4_learning_on_video_first_pack_video/video_13/data/text.txt', 'w' ) # параметр w - write открываем и полностью переписываем файл
# file = open('TASK_4_learning_on_video_first_pack_video/video_13/data/text.txt', 'a' ) # параметр a - append добавление информации
file.write('Hello')
file.write('!!!')
# Перевод на новую строку
file.write('Hello\n')
file.write('!!!')
file.close()
# Ввод инфы пользователем
data = input("Введите текст: ")
file = open('TASK_4_learning_on_video_first_pack_video/video_13/data/text.txt', 'w' )
file.write(data + "\n")
file.close()
file = open('TASK_4_learning_on_video_first_pack_video/video_13/data/text.txt', 'a' )
file.write(data + "\n")
file.write("hello World")
file.write("hello World")
file.write("hello World")
file.close()

file = open('TASK_4_learning_on_video_first_pack_video/video_13/data/text.txt', 'r' ) # параметр r - read чтение
print(file.read())
print(file.read(4)) # указываем сколько символов вывести

# считывать файл построчно
for line in file:
    print(line, end="") # end чтоб убрать энтер последний
file.close()