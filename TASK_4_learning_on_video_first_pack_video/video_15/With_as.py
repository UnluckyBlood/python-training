# try:
#     file = open ('text.txt', 'r')
#     file.read()

# except FileNotFoundError:
#     print("файл не найден!")
# # file не видна в других блоках, ток в try
# finally:
#     file.close

# когда используем with as мы сразу указываем что после он будет закрыт
try:
    with open ('TASK_4_learning_on_video_first_pack_video/video_15/text.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print("файл не найден!")
