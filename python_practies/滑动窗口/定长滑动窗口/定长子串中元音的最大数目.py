class Solution:

    def valid_str(self,s) -> bool:
        match (s):
            case 'a':
               return True
            case 'e':
                return True
            case 'i':
                return True
            case 'u':
                return True
            case 'o':
                return True
        return False


    def maxVowels(self, s: str, k: int) -> int:
        # 1.设置双指针
        slow = 0
        fast = 0
        # 元音字母的个数
        cnt = 0
        max = 0
        # 防止因为指针移动顺序而导致的重复计算
        flag = True
        # 2.当快指针指向最后一个元素的时候就暂停寻找元音字母
        while fast < len(s):
            fast_s = s[fast]

            if self.valid_str(fast_s) and flag:
                cnt+=1


            # 要保持窗口大小
            if fast - slow < k:
                fast+=1
                flag = True
            else:
                # 当移动右边的指针的时候，如果右指指向了元音字母，我们的元音的数量就要减少
                slow_s = s[slow]
                flag = False
                if self.valid_str(slow_s):
                    cnt -= 1
                slow+=1

            max = cnt if max < cnt else max

        return max


def main():
    print(Solution().maxVowels("leetcode",3))
    pass


if __name__ == '__main__':
    main()