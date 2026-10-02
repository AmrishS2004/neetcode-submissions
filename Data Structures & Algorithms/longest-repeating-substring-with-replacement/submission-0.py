class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        l=0
        ml=0
        ms=0

        for r in range(len(s)):
            c[s[r]]=c.get(s[r],0)+1

            ml=max(ml,c[s[r]])
            while((r-l+1-ml)>k):
                c[s[l]]-=1
                l+=1
            ms=max(ms,r-l+1)

        return ms
