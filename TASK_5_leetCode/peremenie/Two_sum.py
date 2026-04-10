# Дан массив целых чисел надо найти из списка два числа при сумме которых получится target
# я решил просто сделать через два фора, мы делаем простой прогон по сути для каждого числа весь список, то есть если взять порядок 1,2,3,4,5 будет выглядеть как 1+1,1+2,1+3...2+1,2+2... один недочёт
# у нас могут взяться одни и теже числа, чтобы этого избежать наверное стоит добавить условие и continue
class Solution:
    def twoSum(self, nums: List[int], target: int):
        for a in range(len(nums)):
            for b in range(len(nums)):
                if nums[a]+nums[b] == target:
                    return a,b
                
check = Solution()
print (check.twoSum([15,13,18,2,36,7,5,34,24,3,16],50))

# вот с этим добавлением у нас не будет случайного срабатывания при суммировании одного и того же индекса
class Solution:
    def twoSum(self, nums: List[int], target: int):
        for a in range(len(nums)):
            for b in range(len(nums)):
                if a==b:continue
                print(a,b)
                if nums[a]+nums[b] == target:
                    return [a,b]
                
check = Solution()
print (check.twoSum([15,13,18,2,36,7,5,34,24,3,16],50))


# самый быстрый способ 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                return [seen[compliment],i]
            seen[num] = i

check = Solution()
print (check.twoSum([15,13,18,2,36,7,5,34,24,3,16],50))