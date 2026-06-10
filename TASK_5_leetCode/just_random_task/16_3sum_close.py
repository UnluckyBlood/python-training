# 16. 3Sum Closest
# Средний
# Темы
# значок премиум-замка
# Компании
# Дан целочисленный массив nums длиной n и целое число target. Найдите три целых числа в различных индексах в nums, сумма которых наиболее близка к target.

# Верните сумму трех целых чисел.

# Можно предположить, что для каждого набора входных данных существует ровно одно решение.

 

# Пример 1:

# Входные данные: nums = [-1,2,1,-4], target = 1
# Выходные данные: 2
# Пояснение: Сумма, наиболее близкая к целевому значению, равна 2. (-1 + 2 + 1 = 2).
# Пример 2:

# Ввод: nums = [0,0,0], target = 1
# Вывод: 0
# Пояснение: Сумма, наиболее близкая к целевому значению, равна 0. (0 + 0 + 0 = 0).
 

# Ограничения:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])
        current = sum(nums[:k])
        if current >= target:
            return current
        current = sum(nums[-k:])
        if current <= target:
            return current
        
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest