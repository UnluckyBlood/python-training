# Contains Duplicate
# Easy
# Topics
# Company Tags
# Hints
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false
# Topics
# Recommended Time & Space Complexity
# Hint 1
# A brute force solution would be to check every element against every other element in the array. This would be an O(n^2) solution. Can you think of a better way?
# Hint 
# Is there a way to check if an element is a duplicate without comparing it to every other element? Maybe there's a data structure that is useful here.
# Hint 3
# We can use a hash data structure like a hash set or hash map to store elements we've already seen. This will allow us to check if an element is a duplicate in constant time.

# я подсмотрел как реализован counter в библиотеки и решил что можно сделать сортировку и если элемент повториться то есть дубликат
nums = [1,5,3,4,88,234,345,234]
def dublicate(nums):
    nums.sort()
    el1 = None
    for i in range(len(nums)):
        el2 = nums[i]
        if el1 == el2:
            return("true")
        el1 = nums[i]
    return ("false")

print(dublicate(nums))

# по скорости выполнения 27 ms на сайте, топ 2 beats 89.96%, по памяти 7,7 MB тоже на втором месте beats 99.53%
# на первом месте по скорости (26 ms) использование set, если в  set найдётся такой же элемент, то тру
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#  на первом месте по памяти тот же пример что и сверху через set

sol = Solution()
sol.hasDuplicate(nums)


# о set
# set в Python — это неупорядоченная коллекция уникальных элементов. Он работает на основе хэш-таблицы, поэтому основные операции (добавление, удаление, проверка наличия) выполняются в среднем за O(1).

# Как устроен set внутри?
# Хэш-функция
# Когда вы добавляете объект в set, Python вычисляет его хэш (hash(obj)). Хэш — это целое число, которое служит «индексом» в таблице.

# Таблица (массив)
# Внутри set есть массив «корзин» (buckets). По хэшу определяется номер корзины, куда помещается элемент.

# Разрешение коллизий
# Если у двух объектов хэш совпадает (или совпадает индекс корзины), используется метод открытой адресации — поиск следующей свободной корзины.

# Рост таблицы
# Когда заполнение превышает порог (обычно 2/3), таблица автоматически увеличивается (примерно в 4 раза, затем в 2 раза) — rehashing: все элементы перехешируются заново.

# Особенности set
# Элементы должны быть хэшируемыми
# Неизменяемые типы: int, float, str, tuple (если внутри тоже хэшируемые).
# Нельзя положить list, dict, set (но можно frozenset).

# Нет порядка (до Python 3.7 порядок был случайным, с 3.7+ сохраняется порядок вставки, но полагаться на это не стоит).

# Быстрая проверка на вхождение: if x in my_set — O(1) в среднем.

# Примеры использования
# python
# # Создание
# s = {1, 2, 3}                # литерал
# s = set([1, 2, 2, 3])        # из списка -> {1, 2, 3}
# s = set()                    # пустое множество (не {} — это словарь!)

# # Добавление
# s.add(4)                     # {1, 2, 3, 4}

# # Удаление
# s.remove(2)                  # если нет — KeyError
# s.discard(5)                 # если нет — ничего не произойдёт

# # Проверка наличия
# if 3 in s:
#     print("есть")

# # Операции
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)   # объединение -> {1,2,3,4,5}
# print(a & b)   # пересечение -> {3}
# print(a - b)   # разность -> {1,2}
# print(a ^ b)   # симметричная разность -> {1,2,4,5}