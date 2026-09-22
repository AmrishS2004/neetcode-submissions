class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c=set(nums)
        b=1
        a=[1]*len(nums)
        d = sorted(list(c))
        if len(d)==0:
            
            return 0
       
    
        for i in range(len(d)-1):
            
            
            if d[i+1]==d[i]+1:
                b=b+1
                
            else:
                b=1
                
            a[i]=b
            
        return max(a)    
