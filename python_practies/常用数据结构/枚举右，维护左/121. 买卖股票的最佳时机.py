from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_input = prices[0]
        max_output = prices[0]


        for price in prices:
            # 枚举左边
            if min_input >= max_output:
                # 只要左边的值要大于我们右边新加入的值，我们就要让其买入时的价格最小
                min_input = max_output

            # 维护右边
            max_output = price

            max_profit = max(max_profit,(max_output - min_input))

        return max_profit



def main():
    s = Solution()
    profit = s.maxProfit([7,1,5,3,6,4])
    print(f"最大利润是：{profit}")
    pass


if __name__ == "__main__":
    main()