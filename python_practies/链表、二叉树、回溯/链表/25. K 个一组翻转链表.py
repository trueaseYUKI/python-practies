from collections import deque
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_nodes(arr:List[int]):
    head = ListNode(val=arr[0])
    temp = head
    for i in range(1,len(arr)):
        node = ListNode(val=arr[i])
        temp.next = node
        temp = temp.next

    return head
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 如果 k == 1不用反转直接返回
        if k == 1:
            return head

        # 先计算当前的链表的长度
        l = head
        length = 0
        while l != None:
            length += 1
            l = l.next

        # 在头结点之前准备一个哨兵
        dummy = ListNode(val=0,next=head)

        pre = dummy
        end = dummy
        cnt = 0
        reversed_cnt = 0
        stack = deque()
        while end != None or length >= k:

            if cnt < k:
                end = end.next
                cnt += 1
            # 当我们的个数刚好等于 k
            elif cnt == k:
                start = pre.next
                # 记录下一组
                next_group = end.next
                for _ in range(0,k):
                    stack.append(start)
                    start = start.next

                temp = stack.pop()

                pre.next = temp
                # 弹栈，反转链表拼接
                while len(stack) > 0:
                    node = stack.pop()
                    temp.next = node
                    temp = temp.next
                    if len(stack) == 0:
                        end = node

                # 拼接下一个组
                temp.next = next_group
                length -= k
                pre = end
                cnt = 0
                reversed_cnt += 1

        return dummy.next




def main():
    head = array_to_nodes([1,2,3,4,5])
    s = Solution()
    res = s.reverseKGroup(head,2)
    print(f"反转后的链表：{res}")

if __name__ == "__main__":
    main()