# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # 计算链表中元素的个数
        n = 0
        temp = head
        while temp != None:
            n += 1
            temp = temp.next

        # 计算最终答案
        ans = 0
        temp = head
        n = n - 1
        while temp != None:
            mid = temp.val * (2 ** n)
            ans += mid
            n -= 1
            temp = temp.next

        return ans


def main():
    s = Solution()
    next2 = ListNode(val=1)
    next1 = ListNode(val=0,next=next2)
    head = ListNode(val=1,next=next1)

    res = s.getDecimalValue(head)
    print(f"十进制：{res}")


if __name__ == "__main__":
    main()