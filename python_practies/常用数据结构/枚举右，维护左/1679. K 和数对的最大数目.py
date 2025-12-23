from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        records = defaultdict(int)

        # 维护左，枚举右
        for right in nums:
            diff = k - right
            # 如果当前这个值并不存在于当前字典中
            if records[diff] == 0:
                # 我们就right指针指向的值保存到字典中
                records[right] += 1
            else:
                # 如果它存在于字典中，我们就将其和right指针指向的值从字典中删除
                records[diff] -= 1
                # 并且将移除的个数+1
                ans += 1

        return ans

def main():
    res = Solution().maxOperations([1,2,3,4],5)
    print(f"最大的操作次数：{res}")
    pass

if __name__ == "__main__":
    main()