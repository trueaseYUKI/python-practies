class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     # 回文数
    #     str_x = str(x)
    #     return str_x[::-1] == str_x

    def isPalindrome(self, x: int) -> bool:

        # 1.如果是负数，那么就直接返回False
        if x < 0: return False

        if x == 0: return True
        # 2.然后求这个数是多少位数
        count = 0

        temp = x
        while temp > 0:
            temp //= 10
            count+=1

        print(f'位数是：{count}')
        tempA = x
        tempB = x
        low_pre_remain = 0
        high_pre_remain = 0
        high = 0
        low = 0
        for i in range(1,count+1):
            # 1.求低位的对应的数字是多少
            tempA //= 10
            remain = x - (tempA * (10 ** i))
            # 上一次留下来的数值

            if i == 1:
                low_pre_remain = remain
                low = remain
            else:
                low = (remain - low_pre_remain) // (10 ** (i - 1))
            pre_remain = remain

            # 2.求高位的数字是多少
            tempB = x
            high_remain = tempB // (10 ** (count - i))

            if i == 1:
                high = high_remain
                high_pre_remain = high_remain
            else:
                remain_pos = high_pre_remain * 10
                high = high_remain - remain_pos
            high_pre_remain = high_remain

            # print(f"低位数字：{low},高位数字：{high}")
            # 只要出现数字不同，就直接返回False
            if low != high:
                return False


        return True


def main():
    solution = Solution()
    isPalindrome = solution.isPalindrome(1234)
    print(f"是否是回文数：{isPalindrome}")

if __name__ == '__main__':
    main()

