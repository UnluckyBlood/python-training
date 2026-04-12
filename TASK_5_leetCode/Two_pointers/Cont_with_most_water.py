# Емкость С Наибольшим Количеством Воды
# Medium
# Темы
# Теги компании
# Подсказки
# Вам дан целочисленный массив heights, где heights[i] обозначает высоту 
# i
# t
# h
# i 
# то
#  й планки.

# Вы можете выбрать любые две планки, чтобы сделать из них контейнер. Верните максимальное количество воды, которое может вместить контейнер.

# Пример 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Пример 2:

# Input: height = [2,2,2]

# Output: 4
# Ограничения:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000

# Это я написал пока хотел понять что правильно понимаю условие задачи
def water(nums)->int:
    tru = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j : continue    
            tru.append(min(nums[i],nums[j])*(j-i))
    return max(tru)
height = [1,7,2,5,4,7,3,6]
print(water(height))

# это чтобы оптимизировать
class Water:
    def height_WATER(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            length = right - left
            height = min(heights[left], heights[right])
            curr_area = length * height
            max_area = max(max_area, curr_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

w = Water()
print (w.height_WATER(height))