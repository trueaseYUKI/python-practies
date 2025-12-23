import math
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        # 对potions进行排序
        potions.sort()

        for spell in spells:
            # 我们只要找到目标值，或者大于目标值第一个值
            target = math.ceil(success / spell)
            # 我们使用我们自己的二分查找
            pos = self.binary_search_first_bigger(potions,target)
            ans.append(len(potions) - pos)
        return ans

    # 找寻第一个大于目标值的位置
    def binary_search_first_bigger(self,array:List[int],target:int):
        left = 0
        right = len(array) - 1

        # 我们要找到第一个大于我们目标值的位置
        # 注意：这里我们允许left==right,因为这样left才会最后超出位置
        while left <= right:
            mid = (left + right) // 2

            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 这里我们返回left，也就是第一个大于target的值
        return left



def main():
    s = Solution()
    success_pair = s.successfulPairs([2],[2,2,3],4)
    print(f"成功的组合个数：{success_pair}")
    pass


if __name__ == "__main__":
    main()
