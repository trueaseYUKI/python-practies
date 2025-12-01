


class Solution:

    def contrast_bracket(self,left_bracket,right_bracket) -> bool:
        if left_bracket == '(' and right_bracket != ')':
            return False
        elif left_bracket == '{' and right_bracket != '}':
            return False
        elif left_bracket == '[' and right_bracket != ']':
            return False

        return True



    def isValid(self, s: str) -> bool:
        # 0.如果字符串的长度不是偶数，则都是不合法的
        if len(s) % 2 != 0:
            return False

        # 1.将字符串拆分为单个字符的列表
        bracket_list = list(s)

        # 2.将左括号入栈，遇到右括号就弹出栈顶元素进行对比
        left_bracket_stack = []


        for bracket in bracket_list:
            match bracket:
                case '(':
                    left_bracket_stack.append(bracket)
                case '{':
                    left_bracket_stack.append(bracket)
                case '[':
                    left_bracket_stack.append(bracket)

            if bracket == ')' or bracket == ']' or bracket == '}':
                if len(left_bracket_stack) > 0:
                    left_bracket = left_bracket_stack.pop()
                    # 与栈顶元素进行对比，只要不匹配返回False
                    if not self.contrast_bracket(left_bracket,bracket):
                        return False
                else:
                    return False


        # 如果对比完毕，栈内依然还有括号，则直接返回False
        if len(left_bracket_stack) > 0:
            return False

        return True



def main():
    s = Solution()
    print(s.isValid("){"))



if __name__ == '__main__':
    main()