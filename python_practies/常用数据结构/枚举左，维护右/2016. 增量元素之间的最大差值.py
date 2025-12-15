from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        i = 0
        max_difference = -1
        for j in range(0,len(nums)):
            if j > i and nums[j] < nums[i]:
                i = j
            else:
                max_difference = max(max_difference, (nums[j] - nums[i]))
                if max_difference == 0:
                    max_difference = -1



        return max_difference



def main():
    s = Solution()
    ans = s.maximumDifference([9,4,3,2])
    print(f"最大差值：{ans}")
    pass

if __name__ == "__main__":
    main()