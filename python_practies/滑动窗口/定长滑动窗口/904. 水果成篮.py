from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        left = 0
        right = 0

        bucket = defaultdict(int)
        kind = 0
        while right < len(fruits):

            # 如果当前品种的树不在字典中
            if bucket[fruits[right]] == 0:
                bucket[fruits[right]] += 1
                kind += 1
            # 如果当前品种的水果在字典中
            else:
                bucket[fruits[right]] += 1
            right += 1

            while kind > 2 and bucket[fruits[left]] > 0:
                bucket[fruits[left]] -= 1
                if bucket[fruits[left]] == 0:
                    kind -= 1
                left += 1


            ans = max(ans,(right - left))

        return ans

def main():
    total = Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4])
    print(f"可以采摘几棵树上的水果：{total}")
    pass

if __name__ == "__main__":
    main()