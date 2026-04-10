# задача требуется доставать наибольшие числа из списка в количестве k штук
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        el = []
        re = nums[:]
        while k>0:
            f = max(set(re), key=re.count)
            el.append(f)
            while f in re:
                re.remove(f)
            k -= 1
        return el
    
#  я придумал слишком медленно

# по времени смог сделать только так 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        re = nums[:]
        while k>0:
            el = {}
            for x in re:
                el[x] = el.get(x, 0) + 1
            f = max(el, key=el.get)
            out.append(f)
            re = [x for x in re if x != f]
            k -=1
        return out


#  самый быстрый, но тут был использован иморт библиотеки, что я избегал
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        result=[]
        m=c.most_common(k)
        for i in m:
            result.append(i[0])
        return result
    

sol = Solution()
nums = [1,1,2,3,5,7,2,4,551,543,1,1,321,132,312,321,32,31,4,2,2,2,45,23,2,1,231,21,33,21,]
k = 3
print(sol.topKFrequent(nums,k))

        

            
        