
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""

        left = 0
        for i in range(0,len(s)):
            if len(s) == (2 * k) and i == len(s) - 1:
                ans += s[left:left + k][::-1]
                ans += s[left + k:]

            if i != 0 and i % (2 * k) == 0 :
                ans += s[left:i - k][::-1]
                if i != len(s) - 1:
                    ans += s[i - k:i]
                else:
                    ans += s[i - k:]
                left = i
            # 如果字符串长度不等于 2 * k 但是i位于最后一位
            elif i == len(s) - 1 and len(s) != (2 * k):
                if k <= i - left + 1 <= (2 * k):
                    ans += s[left:left + k][::-1]
                    ans += s[left + k:]
                elif i - left + 1 < k:
                    ans += s[left:][::-1]

        return ans



def main():
    s = Solution().reverseStr("abcdef",1)
    print(f"反转后的字符串：{s}")
    pass


if __name__ == "__main__":
    main()
