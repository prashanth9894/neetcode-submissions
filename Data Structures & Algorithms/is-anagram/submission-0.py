class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars =[0] * 26
        for n in s:
            chars [ord(n) - 97] +=1
        for n in t:
            chars [ord(n) - 97] -=1
        for Count in chars:
            if Count !=0:
                return False
        return True
        