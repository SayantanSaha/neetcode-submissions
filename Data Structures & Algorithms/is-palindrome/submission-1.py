class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        s = s.lower()
        cs=""
        alfa = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","0"}
        for c in s:
            if c in alfa:
                cs+=c
        l=len(cs)
        l2 = l//2
        for i in range(0,l2):
            if cs[i]!=cs[l-i-1]:
                return False
        return True