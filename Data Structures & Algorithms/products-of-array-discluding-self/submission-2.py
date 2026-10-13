class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        products = [1]*n
        p=1
        q=1
        for i in range(n):
            products[i]=p
            p=p*nums[i]
           
        for j in range(n-1,-1,-1):
            products[j]=products[j]*q
            q=q*nums[j]
            
        return products