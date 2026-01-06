from typing import Optional, List



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 1. 计算链表总长度
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        # 计算基础长度和余数
        base_len = n // k
        remain = n % k

        ans = []
        current = head  # 遍历原链表的指针

        # 遍历k次，分割出k个部分
        for i in range(k):
            # 确定当前部分的长度：前remain个部分长度+1
            curr_len = base_len + 1 if i < remain else base_len
            if curr_len == 0:
                ans.append(None)
                continue

            # 记录当前部分的头节点
            part_head = current
            # 遍历到当前部分的最后一个节点
            for j in range(curr_len - 1):
                if current:
                    current = current.next

            # 截断链表
            if current:
                next_node = current.next
                current.next = None
                current = next_node

            ans.append(part_head)

        return ans


def array_to_nodes(arr:List[int]):
    head = ListNode(val=arr[0])
    temp = head
    for i in range(1,len(arr)):
        node = ListNode(val=arr[i])
        temp.next = node
        temp = temp.next

    return head

def main():
    head = array_to_nodes([1,2,3,4,5,6,7,8,9,10])
    s = Solution()
    res = s.splitListToParts(head,3)
    print(f"分隔后的链表结果：{res}")


if __name__ == "__main__":
    main()