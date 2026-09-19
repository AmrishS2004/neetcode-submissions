class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[1]*n

        left=1
        for i in range(n):
            a[i]=left
            left=left*nums[i]
        right=1
        for i in range(n-1,-1,-1):
            a[i]=right*a[i]
            right=right*nums[i]

        return a