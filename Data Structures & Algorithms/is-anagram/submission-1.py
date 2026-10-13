class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_freq = {}
        for c in s:
            letter_count = letter_freq.get(c,0)
            letter_freq[c] = letter_count+1
        for nc in t:
            nlc = letter_freq.get(nc,-1)
            if nlc<=0:
                return False
            letter_freq[nc]=nlc-1
        for k in letter_freq:
            if letter_freq[k]>0:
                return False
        return True


        