class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = []
        for i in range(len(nums)):
            print(nums[i])
            if val != nums[i]:
                num.append(nums[i])
        
        nums[:] = num
        print(nums)
        return len(nums)
