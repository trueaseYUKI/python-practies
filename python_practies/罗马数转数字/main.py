

class Solution:
    def romanToInt(self, s: str) -> int:

        # 1.我们先定义一个罗马字符对照表
        romance_map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        # 通常情况下，罗马数字中小的数字在大的数字的右边
        # 2.我们第一步，就是将字符串拆分为单个字符，直接转换为列表
        romance_words = list(s)
        if len(romance_words) == 1:
            figure = romance_map[romance_words[0]]
            return figure

        figure = 0
        # 3.我们对照每个位置上的数字和它右边的数字
        for index in range(0,len(romance_words)):
            # 如果当前的位置的数字有右边的数字
            if index + 1 < len(romance_words):
                # 当前位置的数值小于右边
                if romance_map[romance_words[index]] < romance_map[romance_words[index + 1]]:
                    figure -= romance_map[romance_words[index]]
                else:
                    figure += romance_map[romance_words[index]]
            # 最后一位直接加
            else:
                figure += romance_map[romance_words[index]]

        return figure



def main():
   s = Solution()
   s.romanToInt("MCMXCIV")

if __name__ == "__main__":
    main()