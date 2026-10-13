class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, value in enumerate(nums):
            oth_value = target-value
            oth_pos = num_map.get(oth_value,-1)
            if oth_pos!=-1:
                    return [oth_pos[0],index]
            pos = num_map.get(value,[])
            pos.append(index)
            num_map[value] = pos
        return []


        