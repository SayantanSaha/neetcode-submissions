class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums_set = set(nums)
        longest_seq = 0
        for n in nums_set:
            seq_len=1
            if n-1 in nums_set:
                continue
            seq_ele = n
            while seq_ele+1 in nums_set:
                seq_len+=1
                seq_ele+=1
            longest_seq=max(seq_len,longest_seq)
        return longest_seq

