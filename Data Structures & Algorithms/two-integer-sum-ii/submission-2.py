class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while right>left:
            sum = numbers[left]+numbers[right]
            if sum>target:
                right-=1
                continue
            if sum<target:
                left+=1
                continue
            return [left+1, right+1]
            