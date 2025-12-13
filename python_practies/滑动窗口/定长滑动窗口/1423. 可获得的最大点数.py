from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        # 如果 k == cardPoints.length
        l = len(cardPoints)
        if l == k:
           return sum(cardPoints)

        # 我们使用数学的思想，如果不管其当前的点数的大小，我们不同抽卡的结果组合个数为 K + 1

        # 我们先加右边
        window_sum = max_sum = sum(cardPoints[0:k])
        for i in range(0,k):
            # 移除窗口的数值
            window_sum -= cardPoints[k - i - 1]
            # 加入窗口的数值
            window_sum += cardPoints[l - i - 1]

            max_sum = max(max_sum,window_sum)


        return max_sum

def main():
    max = Solution().maxScore([1,1,200,1,1,1,79,1],3)
    print(f"最大值：{max}")
    pass


if __name__ == '__main__':
    main()
    pass