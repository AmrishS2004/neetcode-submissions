class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for i in strs:
            res.append(str(len(i))+"#"+i)
        return "".join(res)

        

    def decode(self, s: str) -> List[str]:
        res,i=[],0
        while i<len(s):
            j=i
            while s[j]!="#":
                j=j+1
            a=int(s[i:j])

            word=s[j+1:a+j+1]
            res.append(word)
            i=j+1+a
        return res

        