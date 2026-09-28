class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False

        w={}
        c={}
        for i in s1:
            c[i]=c.get(i,0)+1
        l=0
        for i in range(len(s2)):
            w[s2[i]]=w.get(s2[i],0)+1

            if((i-l+1)>len(s1)):
                w[s2[l]]-=1

                if(w[s2[l]]==0):
                    del w[s2[l]]
                l+=1
            if (c==w):
                return True
        return False