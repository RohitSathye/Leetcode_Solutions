class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        Anag = False
        
        if len(s) == len(t):
            for i in s:
                if i in t:
                    Anag = True
                    t.remove(i)
                else:
                    Anag = False
                    break
        else:
            Anag = False   
        
        return Anag
     