

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 将字符串转换为列表
        s_list = list(s)

        if len(s) == 1 or len(s) == 0:
            return len(s)

        # 设置双指针
        left = 0
        right = 0
        # 最大子串长度
        max = 0

        # 设置不重复的集合
        s_distinct = set()

        # 在不等于0的情况下不等
        while True:
            if right >= len(s) or left >= len(s):
                break
            # 如果字符不在集合中，移动右指针
            if s_list[right] not in s_distinct:
                s_distinct.add(s_list[right])
                if right < len(s):
                    right+=1
            # 如果字符在集合中，移动左指针
            else:
                s_distinct.remove(s_list[left])
                if left < len(s) - 1:
                    left+=1

            max = right - left if (right - left) > max else max

        return max







def main():
    max_sub =Solution().lengthOfLongestSubstring("abcde")
    print(f"最大字串长度：{max_sub}")
    pass


if __name__ == "__main__":
    main()
    pass