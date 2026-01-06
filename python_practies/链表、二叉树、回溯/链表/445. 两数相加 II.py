from collections import deque
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 反转两个链表
        head1 = self.reverse_list(l1)
        head2 = self.reverse_list(l2)

        # 计算两个链表的长度
        length1 = 0
        length2 = 0
        cur1 = head1
        cur2 = head2

        while cur1 != None:
            length1 += 1
            cur1 = cur1.next

        while cur2 != None:
            length2 += 1
            cur2 = cur2.next

        # 比出最小长度
        min_length = min(length1,length2)

        # 进行加法
        cur1 = head1
        cur2 = head2
        head = None
        pre = 0
        temp = head
        for _ in range(0,min_length):
            left = cur1.val
            right = cur2.val

            two_sum = left + right
            # 如果上一个数字进位了
            if pre >= 10:
                two_sum += 1
                pre = two_sum
                if two_sum >= 10:
                    node = ListNode(val=two_sum - 10)
                    if temp == None:
                        temp = node
                        head = temp
                    else:
                        temp.next = node
                        temp = temp.next
                else:
                    node = ListNode(val=two_sum)
                    if temp == None:
                        temp = node
                        head = temp
                    else:
                        temp.next = node
                        temp = temp.next
            else:
                pre = two_sum
                if two_sum >= 10:
                    node = ListNode(val=two_sum - 10)
                    if temp == None:
                        temp = node
                        head = temp
                    else:
                        temp.next = node
                        temp = temp.next
                else:
                    node = ListNode(val=two_sum)
                    if temp == None:
                        temp = node
                        head = temp
                    else:
                        temp.next = node
                        temp = temp.next

            cur1 = cur1.next
            cur2 = cur2.next

        max_length = max(length1,length2)
        remain_length = max_length - min_length
        cur1 = cur2 if cur2 != None else cur1

        if remain_length == 0 and pre >= 10:
            node = ListNode(val=1)
            temp.next = node


        # 最后来判断是否还有进位
        for _ in range(0,remain_length):
            if pre >= 10:
                two_sum = cur1.val + 1
                pre = two_sum
                if two_sum >= 10:
                    node = ListNode(val=two_sum - 10)
                    if temp == None:
                        temp = node
                        head = temp
                    else:
                        temp.next = node
                        temp = temp.next
                else:
                    node = ListNode(val=two_sum)
                    temp.next = node
                    temp = temp.next
            else:
                node = ListNode(val=cur1.val)
                temp.next = node
                temp = temp.next
            cur1 = cur1.next

        if pre >= 10:
            node = ListNode(val=1)
            temp.next = node


        head = self.reverse_list(head)
        return head

    def reverse_list(self,head:Optional[ListNode]) -> ListNode:
        stack = deque()
        p = head

        while p != None:
            stack.append(p)
            p = p.next

        temp = stack.pop()
        head = temp
        while len(stack) != 0:
            node = stack.pop()
            temp.next = node
            temp = temp.next
        temp.next = None

        return head


def array_to_nodes(arr:List[int]):
    head = ListNode(val=arr[0])
    temp = head
    for i in range(1,len(arr)):
        node = ListNode(val=arr[i])
        temp.next = node
        temp = temp.next

    return head

def main():
    head1 = array_to_nodes([2])
    head2 = array_to_nodes([8,9,9])
    s = Solution()
    res = s.addTwoNumbers(head1,head2)
    print(f"两数相加：{res}")


if __name__ == "__main__":
    main()