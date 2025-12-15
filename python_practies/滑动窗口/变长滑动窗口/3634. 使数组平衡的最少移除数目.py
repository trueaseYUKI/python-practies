from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        left = 0
        max_len = 1  # 至少一个元素一定合法

        for right in range(n):
            # 如果不满足条件，就缩小窗口
            while nums[left] * k < nums[right]:
                left += 1

            # 更新最大合法窗口
            max_len = max(max_len, right - left + 1)

        return n - max_len





def main():
    ans = Solution().minRemoval([2,1,5],2)
    print(f"最少移除的元素个数：{ans}")
    pass


if __name__ == "__main__":
    main()
