from collections import defaultdict
from typing import List, Dict, Tuple


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for d in dominoes:
            d = tuple(sorted(d))  # 只有两个数，排序是 O(1) 的
            ans += cnt[d]
            cnt[d] += 1
        return ans
def main():
    s = Solution()
    sum_num = s.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]])
    print(f"等价多米诺骨牌的数量：{sum_num}")
    pass


if __name__ == "__main__":
    main()