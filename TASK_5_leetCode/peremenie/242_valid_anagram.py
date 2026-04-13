# даётся два списка, и надо определить являются ли они анаграммой друг другу (теже символы но в другом порядке)

# В самом начале переведём текст в список, так как может у нас слова, а может отдельные символы в списке
# Я решил реализовать что в начале проверяем длину списка, чтобы если список уже этим отличается не тратить время (да, в правильных по длине списка будет плюс итерация, но в остальных лсучаях поможет)
# потом проходясь по каждому символу из второго списка мы проходимся, и пробуем его удалить из первого списка если там он есть, если нету, то у нас сработает except и вернёт ошибку
# и в конце если все условия выполнились мы возвращаем True
def isAnagram(list1,list2):
    list1 = list(list1)
    list2 = list(list2)
    print(list1,list2)
    if len(list1)!=len(list2):
        print(list1,list2)
        return False
    for i in list2:
        print(list1,list2)
        try:  
            list1.remove(i)
            print(list1,list2)
        except :
            print(list1,list2)
            return False
    return True


print(isAnagram(["a","r","a","r"],["a","r","a"]))
print(isAnagram(["a","r","a"],["a","r","a"]))
print(isAnagram(["a","r","a"],["a","r","G"]))
print(isAnagram(["r","a","a","a","r","a"],["a","r","a","a","r","a"]))
print(isAnagram(list("anagram"),list("nagaram")))

# так как это слишком сложный метод, он не подходит
# вот проще увидел в инете
def isAnagramLite(list1,list2):
    if sorted(list1) == sorted(list2):
        return True
    return False

print(isAnagramLite(["a","r","a","r"],["a","r","a"]))
print(isAnagramLite(["a","r","a"],["a","r","a"]))
print(isAnagramLite(["a","r","a"],["a","r","G"]))
print(isAnagramLite(["r","a","a","a","r","a"],["a","r","a","a","r","a"]))
print(isAnagramLite(list("anagram"),list("nagaram")))

# этот метод тоже медленный, вот самый быстрый

def isAnagramSpeed(s,t) -> bool:
    if len(s)!=len(t):return False
    for i in set(s):
        if s.count(i)!=t.count(i):return False
    return True
print(isAnagramSpeed(["a","r","a","r"],["a","r","a"]))
print(isAnagramSpeed(["a","r","a"],["a","r","a"]))
print(isAnagramSpeed(["a","r","a"],["a","r","G"]))
print(isAnagramSpeed(["r","a","a","a","r","a"],["a","r","a","a","r","a"]))
print(isAnagramSpeed(list("anagram"),list("nagaram")))