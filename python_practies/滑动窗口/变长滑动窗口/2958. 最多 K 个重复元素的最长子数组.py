from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        records = defaultdict(int)
        left = 0

        for right in range(0,len(nums)):

            records[nums[right]] += 1
            # 窗口内的重复元素个数超出了上限的话
            while records[nums[right]] > k:
                records[nums[left]] -= 1
                left += 1

            ans = max(ans,right - left + 1)

        return ans


def main():
    res = Solution().maxSubarrayLength([1,2,3,1,2,3,1,2],2)
    print(f"最长 好数组 长度：{res}")
    pass

if __name__ == "__main__":
    main()