from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])

        max = 0
        sum = 0
        # 我们先计算出一个窗口的平均值
        for i in range(0,k):
            sum += nums[i]

        max = float(sum / k)

        # 第一个窗口平均值计算完毕之后，我们移动窗口来进行不同的窗口计算
        for i in range(k,len(nums)):
            # 我们的窗口每次移动一格
            sum += nums[i]
            sum -= nums[i - k]
            max = max if max > float(sum / k) else float(sum / k)


        return max


def main():
    print(Solution().findMaxAverage([1,12,-5,-6,50,3],4))
    pass

if __name__ == '__main__':
    main()