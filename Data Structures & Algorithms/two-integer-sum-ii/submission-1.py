class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_dict = {}
        length = len(numbers)
        for i in range(0,length):
            n=numbers[i]
            com = target-n
            if com in numbers_dict:
                return [numbers_dict[com][0]+1,i+1]
            pos=numbers_dict.get(n,[])
            pos.append(i)
            numbers_dict[n]=pos