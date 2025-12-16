from collections import defaultdict
from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:

        # w 是窗口大小，m 是窗口中允许重复的次数
        cnt = defaultdict(int)

        # left 、right 表示天数范围
        left = 0
        right = 0
        ans = 0
        del_list = [False] * len(arrivals)


        # 先求第一个窗口
        for i in range(0,w):
            if cnt[arrivals[i]] < m:
                cnt[arrivals[i]] += 1
            # 当第一个窗口发现重复的次数大于我们的
            # 将丢弃个数 +1 ，并且将我们丢弃的最大天数记录下来
            else:
                del_list[i] = True
                ans += 1
            right += 1



        while right < len(arrivals):

            # 当天数大于窗口的最大范围
            if right - left + 1 > w:
                if cnt[arrivals[left]] > 0 and not del_list[left]:
                    cnt[arrivals[left]] -= 1
                left += 1

            if right - left + 1 <= w and cnt[arrivals[right]] < m:
                cnt[arrivals[right]] += 1
            elif cnt[arrivals[right]] >= m:
                ans += 1
                del_list[right] = True
            right += 1


        return ans



def main():
    s = Solution()
    min_discard = s.minArrivalsToDiscard([7,3,9,9,7,3,5,9,7,2,6,10,9,7,9,1,3,6,2,4,6,2,6,8,4,8,2,7,5,6],10,1)
    print(f"最小丢弃个数：{min_discard}")


if __name__ == "__main__":
    main()