from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        distinct = dict()

        max = 0
        sum = 0
        # 重复的数值的个数
        cnt = 0

        # 先求一个窗口内子数组的和
        for i in range(0,k):
            sum += nums[i]
            # 如果数值在哈希表中，且不是第一次加入哈希表
            if nums[i] in distinct:
                distinct[nums[i]] += 1
                # 重复值数量 +1
                cnt += 1
            else:
                distinct[nums[i]] = 1


        if cnt == 0:
            max = sum


        for i in range(k,len(nums)):

            sum -= nums[i - k]
            sum += nums[i]

            # 如果数值在哈希表中不存在，或者之前存在过，但是已经退出窗口了
            if nums[i] not in distinct or distinct[nums[i]] == 0:
                distinct[nums[i]] = 1
            # 如果数值在哈希表中存在，或者它的数量不等于0
            else:
                distinct[nums[i]] += 1
                cnt += 1


            # 如果数值在哈希表中的数量大于1（则说明它存在重复的）等于和小于1都是不重复
            if distinct[nums[i - k]] > 1:
                distinct[nums[i - k]] -= 1
                cnt -= 1
            else:
                # 小于等于1的时候，我们要让哈希表中的数量值 -1
                distinct[nums[i - k]] -= 1



            # 如果重复数量等于0，则赋值max
            if cnt == 0:
                max = sum if sum > max else max

        return max



def main():
    max = Solution().maximumSubarraySum([9,18,10,13,17,9,19,2,1,18], 5)
    print(f"最大值：{max}")
    pass


if __name__ == '__main__':
    main()
    pass