"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""
from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(0,len(nums)):
    #         for j in range(i + 1,len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i,j]

    def twoSum(self,nums: List[int], target: int) -> List[int]:
        for i in range(0,len((nums))):
            # 我们先求出差值是
            remain_num = target - nums[i]
            # 然后看其是否在列表中，如果不存在就继续求下一个（要剔除当前这个位置）
            if remain_num in nums[i+1:]:
                # 如果它在列表中的话，就返回这个值出现的位置（注意：由于是列表的子列表，所以我们要+i+1，因为它的下标经过切分后从0开始）
                return [i,nums[i+1:].index(remain_num)+i+1]



def main():
   solution =  Solution()
   result = solution.twoSum([3,3],6)
   print(f"结果为：{result}")

if __name__ == "__main__":

    main()
