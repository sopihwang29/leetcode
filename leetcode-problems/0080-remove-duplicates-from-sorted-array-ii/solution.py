class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        times = 1
        if len(nums) <= 2:
            return len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                times += 1
            elif nums[i] != nums[i-1]:
                times = 1

            if times <= 2:
                nums[index] = nums[i]
                index += 1
        return index

                
                
