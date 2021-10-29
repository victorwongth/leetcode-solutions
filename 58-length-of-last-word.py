class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        initiated = False
        length = 0 
        for i in range(len(s)):
            if s[-i-1] != " ":
                print(i, s[-i-1])
                initiated = True
                length += 1
            elif initiated == True:
                break
        return length
      
     def oneLiner(self, s: str) -> int:
         return 0 if not s.split() else len(s.split()[-1])
