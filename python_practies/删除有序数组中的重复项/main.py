from typing import List




class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 利用双指针
        k = 1

        # 如果数组只有一个元素
        if len(nums) == 1:
            return k
        # 如果列表有多个元素
        else:
            for i in range(1,len(nums)):
                # 如果当前的指针位置的值相同，就让快指针后移
                if nums[i-1] == nums[i]:
                    continue
                else:
                    # 将不同的值赋值到最开始相同值的位置
                    nums[k] = nums[i]
                    k+=1

        return k




def main():
    print(Solution().removeDuplicates([1,1,2,2,3,3,4]))
    pass

if __name__ == '__main__':
    main()