class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        products = [1]*n
        p=1
        q=1
        for i in range(0,n-1):
            p=p*nums[i]
            products[i+1]=p
        for j in range(n-1,0,-1):
            q=q*nums[j]
            products[j-1]=products[j-1]*q
        return products