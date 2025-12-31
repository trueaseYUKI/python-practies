from collections import deque
from typing import Optional, List


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
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        fast = head
        sum_group = 0
        cnt = 0
        last_group_cnt = 0
        while fast != None:
            if cnt == sum_group:
                cnt = 0
                sum_group += 1
            fast = fast.next
            cnt += 1

        # 记录最后一组个数
        last_group_cnt = cnt

        fast = head
        slow = head
        group = 1
        group_cnt = 1
        stack = deque[ListNode]()
        while fast != None:
            # 如果是偶数组
            if group % 2 == 0 or (group == sum_group and last_group_cnt % 2 == 0):
                end = fast
                group_cnt = 0
                # 我们判断下当前组是否存在Null的,如果有Null就说明到了最后一组，并且最后一组的个数不够
                for _ in range(0, group):
                    if end == None:
                        break
                    else:
                        stack.append(end)
                        end = end.next
                        group_cnt += 1

                # 如果个数不是偶数则说明个数是不够的
                if group_cnt % 2 != 0:
                    break

                # 如果个数是偶数，则说明反转的个数还是够的，我们就进行反转
                begin = slow
                next_group = end

                # 进行局部反转
                temp = stack.pop()
                # 将第一个结点拼接到前一个组的最后一个结点的后面
                begin.next = temp
                while len(stack) != 0:
                    node = stack.pop()
                    temp.next = node
                    temp = temp.next

                # 将当前组的最后一个元素连接下一个组
                temp.next = next_group
                fast = temp

            if group == group_cnt:
                group += 1
                group_cnt = 0
                slow = fast

            fast = fast.next
            group_cnt += 1
        return head


def main():
    head = array_to_nodes([1,1,0,6,5])
    s = Solution()
    res = s.reverseEvenLengthGroups(head)
    print(f"反转后的链表：{res}")

if __name__ == "__main__":
    main()