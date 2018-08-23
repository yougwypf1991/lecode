class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # mothod 1
        # ret = []
        # l = len(nums)
        # for i in range(l):
        #     for j in range(i + 1, l):
        #         if nums[i] + nums[j] == target:
        #             return i, j
        #         else:
        #             continue
        # mothod 2
        l = len(nums)
        for i in range(l):
            rem = target - nums[i]
            if rem in nums and nums.index(rem) != i:
                return i, nums.index(rem)
            
if __name__ == '__main__':
    s = Solution()
    i, j = s.twoSum([2, 7, 11, 15], 9)
    print([i,j])
