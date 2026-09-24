class Solution:
    def maxProfit(self, p: List[int]) -> int:
        a=set(p)
        b=0

        l,r=0,1
        while r<len(p):
            if p[l]<p[r]:
                b=max(b,(p[r]-p[l]))
                
                
            else:
                l=r
            r+=1
        return b

