from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        distinct_num = dict()

        value_sum = 0
        cnt = 0
        max = 0
        for i in range(0,k):
            # 如果值在字典内不存在就说明这个值与其他值不同，那么就让不同个数+1
            if nums[i] not in distinct_num or distinct_num[nums[i]] == 0:
                cnt += 1
                distinct_num[nums[i]] = 1
            # 如果值在字典内存在，就让这个值 +1
            else:
                # 不能重复减少
                distinct_num[nums[i]] += 1
                if distinct_num[nums[i]] == 1:
                    cnt -= 1


            value_sum += nums[i]

        if cnt >= m:
            max = value_sum


        for i in range(k,len(nums)):
            # 让窗口前进
            value_sum -= nums[i-k]
            value_sum += nums[i]

            # 查看退出窗口的数值，在窗口内有多少个相同的数值
            if distinct_num[nums[i-k]] >= 1:
                distinct_num[nums[i-k]] -= 1
                if distinct_num[nums[i - k]] == 0:
                    cnt -= 1


            # 如果值在字典内不存在就说明这个值与其他值不同，那么就让不同个数+1
            if nums[i] not in distinct_num or distinct_num[nums[i]] == 0:
                cnt += 1
                distinct_num[nums[i]] = 1
            # 如果值在字典内存在，就让这个值 +1
            else:
                # 不能重复减少
                distinct_num[nums[i]] += 1
                if distinct_num[nums[i]] == 1 and cnt != 0:
                    cnt -= 1



            if cnt >= m:
                max = max if max >= value_sum else value_sum

        return max


def main():
    print(Solution().maxSum([1,1,1,2],2,4))
    pass


if __name__ == '__main__':
    main()
    pass