from collections import defaultdict
from typing import List, Dict

from typing import List, Dict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        # 字典值为 (max1, max2)：max1 ≥ max2，初始为 (-∞, -∞)
        digit_extremes: Dict[int, tuple[int, int]] = {}

        for num in nums:
            # 计算数位和（复用你的digit_sum函数）
            ds = self.digit_sum(num)

            # 初始化：若数位和未记录，初始最大/次大为 (-∞, -∞)
            if ds not in digit_extremes:
                digit_extremes[ds] = (-1, -1)  # 用-1适配非负整数场景（题目nums应为非负）
            current_max1, current_max2 = digit_extremes[ds]

            # 核心：O(1)时间更新max1和max2
            if num > current_max1:
                # 新数比当前最大大 → 原max1降级为次大，新数成最大
                new_max2 = current_max1
                new_max1 = num
            elif num > current_max2:
                # 新数介于max1和max2之间 → 仅更新次大
                new_max2 = num
                new_max1 = current_max1
            else:
                # 新数比次大还小 → 不更新
                new_max1, new_max2 = current_max1, current_max2

            # 回写更新后的max1/max2
            digit_extremes[ds] = (new_max1, new_max2)

            # 若当前数位和已有两个有效数（max2≠-1），更新全局最大值
            if new_max2 != -1:
                ans = max(ans, new_max1 + new_max2)

        return ans

    # 复用你的数位和计算函数（已优化）
    def digit_sum(self, num: int) -> int:
        s = 0
        if num == 0:
            return 0
        num = abs(num)
        while num > 0:
            s += num % 10
            num = num // 10
        return s

def main():
    s = Solution()
    max_val = s.maximumSum([18,43,36,13,7])
    print(f"数位和的最大值是：{max_val}")
    pass


if __name__ == "__main__":
    main()