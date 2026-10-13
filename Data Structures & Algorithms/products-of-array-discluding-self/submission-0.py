class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]*len(nums)
        p=1
        q=1
        for i in range(0,len(nums)-1):
            p=p*nums[i]
            products[i+1]=p
        for j in range(len(nums)-1,0,-1):
            q=q*nums[j]
            products[j-1]=products[j-1]*q
        return products