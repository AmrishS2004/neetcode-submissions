from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C=Counter(nums)
        f=[[]for _ in range(len(nums)+1)]

        for nums,i in C.items():
            f[i].append(nums)
        
        res=[]
        for i in range(len(f)-1,0,-1):
            for j in f[i]:
                res.append(j)
                if len(res)==k:
                    return res