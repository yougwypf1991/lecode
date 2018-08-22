class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # to save result
        res_list = []
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # now nums = [-4, -1, -1, 0, 1, 2]
            if nums[i] > 0:
                break
            # if nums[i] == nums[i-1], continue. because a num only caculate 1 time
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # save position of i
            j = i + 1
            # the position of last element
            k = len(nums) - 1
            while j < k:
                # jugment
                if nums[j] + nums[k] == -nums[i]:
                    # save to res_list
                    res_list.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list


if __name__ == '__main__':
    s = Solution()
    result_list = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(result_list)
