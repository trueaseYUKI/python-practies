
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        ans = 0

        # 找出第一个满足条件的窗口
        max_len = min(len(s),len(t))
        right = 0
        left = 0
        cost_sum = 0

        while right < max_len:
            diff = abs(ord(s[left]) - ord(t[left]))
            # 我们要找一段最长子串的开销总和 <= maxCost
            if cost_sum <= maxCost:
                cost_sum += diff
                right+=1

            while cost_sum > maxCost:
                cost_sum -= diff
                left += 1


            ans = max(ans, right - left)

        return ans



def main():
    s = Solution()
    max_cnt = s.equalSubstring("abcd","bcdf",3)
    print(f"满足条件的最大长度：{max_cnt}")
    pass

if __name__ == "__main__":
    main()