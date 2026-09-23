class Solution:
    def trap(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        out=0
        z=h[l]
        t=h[r]

        while l<r:
            w=l-r
            if z<t:
                l+=1
                z=max(z,h[l])
                out+=z-h[l]
                print(out)
            else:
                r-=1
                t=max(t,h[r])
                out+=t-h[r]
        return out


