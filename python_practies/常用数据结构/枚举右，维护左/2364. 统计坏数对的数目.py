from collections import defaultdict
from typing import List


class Solution:

    # 暴力解法
    def countBadPairs_violent(self, nums: List[int]) -> int:
        # 反向思维，我们求出一个数组中下标的所有组合，然后减去j - i == nums[j] - nums[i]的组合即可
        n = len(nums)
        # 总组合数
        total = n * (n - 1) // 2
        # j - i == nums[j] - nums[i] 个数
        cnt = 0

        for l in range(0,n):
            for r in range(l + 1,n):
                if r - l == nums[r] - nums[l]:
                    cnt += 1


        # 我们返回总组合数 - 非题目要求的组合数
        return total - cnt



    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        cnt = 0
        records = defaultdict(int)

        # l < r  r - l == nums[r] - nums[l]
        # 即 r - nums[r] == l - nums[l]
        for r in range(0,n):
            # 将对应的差值数量记录到字典中
            records[nums[r] - r] += 1

            # 如果对应的差值在记录中
            if records[nums[r] - r] > 1:
                cnt += 1


        # 我们返回总组合数 - 非题目要求的组合数
        return total - (cnt + 1) * cnt // 2


def main():
    s = Solution()
    bad_pair = s.countBadPairs([4,1,3,3])
    print(f"坏数对的对数：{bad_pair}")

if __name__ == "__main__":
    main()
