from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        distinct = defaultdict(int)

        left = 0
        right = 0
        max_len = 0

        while True:
            # 当左边指针 >= 右边指针 并且右边指针不指向第一个元素时
            if left >= right and right != 0 or right >= len(s):
                break

            # 当字符在字典中的个数小于2时
            if right <= len(s) - 1 and distinct[s[right]] <= 2:
                distinct[s[right]] += 1
                # 如果右指针移动完毕之后，导致字典中字符的个数超过了2
                if distinct[s[right]] > 2:
                    # 移动左指针，直到字典中它的个数不超过2个
                    while distinct[s[right]] > 2 and left < len(s):
                        distinct[s[left]] -= 1
                        left += 1

                if right < len(s):
                    right += 1

            max_len = max((right - left),max_len)

        return max_len





def main():
    max_len = Solution().maximumLengthSubstring("bcbbbcba")
    print(f"最大的长度：{max_len}")
    pass


if __name__ == '__main__':
    main()