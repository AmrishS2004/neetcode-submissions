class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        a=0

        while l<r:
            h=min(heights[l],heights[r])
            w=r-l
            c_area=h*w
            a=max(a,c_area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return a
