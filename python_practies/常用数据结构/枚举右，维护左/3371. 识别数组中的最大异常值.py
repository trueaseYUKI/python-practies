from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        ans = -inf
        # 当我们从数组和中移除异常值时候，我们的数组和 = 2 * 特殊值之和
        total_sum = 0
        records = defaultdict(int)
        # 求数组总和
        for num in nums:
            total_sum += num
            records[num] += 1

        for r in nums:
            total_sum -= r
            possible = total_sum % 2
            # 如果是0的话说明刚刚移除的可能是异常值
            if possible == 0:
                # 可能的特殊值之和
                sepc_sum = total_sum // 2
                # 如果和当前的值相等（我们要注意可能存在和特殊值之和相同的异常值）
                if sepc_sum == r and records[sepc_sum] > 1:
                    ans = max(ans, r)
                elif sepc_sum != r and records[sepc_sum] > 0:
                    ans = max(ans, r)

            total_sum += r

        return ans


def main():
    s = Solution()
    res = s.getLargestOutlier([6,-31,50,-35,41,37,-42,13])
    print(f"最大的异常值：{res}")


if __name__ == "__main__":
    main()