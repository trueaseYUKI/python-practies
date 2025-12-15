from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        right = 0
        cnt = 0
        nums_len = len(nums)
        ans = 0

        # 只有 0 或 只有 1
        if len(set(nums)) == 1:
            if nums[0] == 0:
                return ans
            else:
                return nums_len - 1

        while right < nums_len and left <= right:
            # 如果我们的窗口内有不止一个0，那就缩小窗口，直到只有一个0
            while cnt < right - left - 1 and right != 0:
                cnt -= nums[left]
                left+=1

            cnt += nums[right]
            right+=1

            ans = max(ans,cnt)


        return ans



def main():
    s = Solution()
    max_len = s.longestSubarray([1,1,1])
    print(f"最大 1 的子数组长度：{max_len}")
    pass


if __name__ == "__main__":
    main()