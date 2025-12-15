from collections import defaultdict
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        k = -1
        distinct = set()
        for i in range(0,len(nums)):
            # 如果对应的绝对值不在字典中
            if nums[i] < 0 and abs(nums[i]) not in distinct:
                distinct.add(abs(nums[i]))

        nums = set(nums)
        result = nums & distinct
        if len(result) != 0:
            k = max(result)

        return k



def main():
    k = Solution().findMaxK([-10,8,6,7,-2,-3])
    print(f"最大的k：{k}")
    pass

if __name__ == "__main__":
    main()
    pass