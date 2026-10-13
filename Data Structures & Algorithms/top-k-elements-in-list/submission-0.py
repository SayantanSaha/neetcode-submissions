import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            count = num_freq.get(num,0)
            num_freq[num] = count+1
        top_k = heapq.nlargest(k, num_freq.items(), key=lambda i: i[1])
        result = []
        for t in top_k:
            result.append(t[0])
        return result