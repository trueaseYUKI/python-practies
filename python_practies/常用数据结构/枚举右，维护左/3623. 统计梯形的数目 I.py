import math
from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # 能组成斜率平行 x 轴的直线的点的相同特征(x1,y1) 和 (x2,y2) y1 == y2  x1 != x2（因为题目中保证每个点坐标不同）
        # 而我们需要4个点才能组成梯形，当我们不同y值有多个点的时候，我们的
        # 我们经过归纳法发现
        """
        假设有3组不同的y值，a1 = 3(第一组的y值组合)、a2=3、a3 = 1
        total += 3 * 0 = 0 pre = 3
        total += 3 * 3 = 9 pre = 6
        total += 1 * 6 = 6 pre = 15 
        """
        # 存储不同的y值
        ans = 0
        diff_y = defaultdict(int)

        # 我们将不同y的个数进行分组加和
        for point in points:
            y = point[1]
            diff_y[y] += 1


        pre = 0
        for cnt in diff_y.values():
            # 求出组合(每次选两个点，组合个数是多少)
            # 当我们当前y的个数 >= 2 时，我们就用组合，小于就 = 0
            n = math.comb(cnt,2) if cnt >= 2 else 0
            ans += n * pre
            pre += n

        return ans


def main():
    s = Solution()
    total = s.countTrapezoids([[50,-41],[64,-66],[-45,-41],[-58,10],[25,10]])
    print(f"梯形总数：{total}")

if __name__ == "__main__":
    main()