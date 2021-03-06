class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        temp = []
        for j in range(length):
            temp.append(nums[j])
            
        while i < length:
            pos = (i+k)%length
            nums[pos] = temp[i]
            i = i + 1
