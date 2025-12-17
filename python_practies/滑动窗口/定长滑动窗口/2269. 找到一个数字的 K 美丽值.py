


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        nums_str = str(num)


        left = right = 0

        while right < len(nums_str):

            if right - left + 1 == k and right < len(nums_str):
                sub = int(nums_str[left:right+1])
                if sub == 0:
                    left += 1
                else:
                    if num % sub == 0:
                        ans += 1
                    left += 1
            else:
                right += 1


        return ans


def main():
    s = Solution()
    ans = s.divisorSubstrings(240,2)
    print(f"最长的字符串：{ans}")

if __name__ == "__main__":
    main()
