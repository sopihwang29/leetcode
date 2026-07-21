class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer = m-1
        pointer2 = n-1
        index = m+n-1

        while pointer >= 0 and pointer2 >= 0:
            print(nums1[pointer], nums2[pointer2])
            if nums1[pointer] <= nums2[pointer2]:
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
            else:
                nums1[index] = nums1[pointer]
                pointer -= 1
            index -= 1
        while pointer2 >= 0:
            nums1[index] = nums2[pointer2]
            pointer2 -= 1
            index -= 1
        print(nums1)

            
