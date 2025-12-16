from math import inf
from typing import List




class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        dist = 0
        min_val,max_val  = inf, -inf

        for arr in arrays:
            dist = max(dist,arr[-1] - min_val, max_val - arr[0])
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])


        return dist



dist = Solution().maxDistance([[5,8],[3,7],[1,9]])
print(f"最长距离：{dist}")