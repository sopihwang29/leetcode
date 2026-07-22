class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        places = []
        for i in range(len(nums)):
            places.append([nums[i], (i + k) % len(nums)])
        for i in range(len(nums)):
            nums[places[i][1]] = places[i][0]
        print(nums)
