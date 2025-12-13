from typing import List, Dict, Tuple


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 好数对集合
        good_nums_dict : Dict[int,List] = {}
        # 好数对个数
        cnt = 0

        for index,num in enumerate(nums):
          # 首次加入字典中的数值的下标肯定是靠前的（要利用下标有序这个条件）
           if num not in good_nums_dict:
               good_nums_dict[num] = []
               good_nums_dict[num].append(index)
          # 第二次加入的下标肯定是靠后的
           else:
               # 我们后面加入的数值的下标肯定是靠后的，那么和前面的下标可以组成的好数对，就有 len(重复数组的长度) 个组合
               cnt += len(good_nums_dict[num])
               good_nums_dict[num].append(index)

        return cnt




def main():
    res = Solution().numIdenticalPairs([1,2,3])
    print(f"好数对个数：{res}")



if __name__ == "__main__":
    main()
    pass