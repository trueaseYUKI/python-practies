from typing import List


class Solution:

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        这里需要明白一个数学规律，当我们的元素值 x 改变
        x - k = min_val <= x <= max_val = x + k
        则 max_val - min_val <= 2 * k
        当  max_val - min_val <= 2 * k 说明当前 x 值都可以与其他值调整到同一个值

        而进行排序之后，就是让当前窗口的最大值 - 最小值满足 <= 2 * k就可以
        """
        # nums[i] 的替换长度是2k
        ans = 0
        l = 0
        # 排序
        nums.sort()
        for r in range(0, len(nums)):
            # 当窗口不满足条件的时候，缩小窗口，窗口满足条件
            while nums[r] - nums[l] > 2 * k:
                l += 1
            ans = max(ans, r - l + 1)

        return ans


def main():
    s = Solution()
    res = s.maximumBeauty([100000],0)
    print(f"最大子序列长度：{res}")
    pass


if __name__ == "__main__":
    main()