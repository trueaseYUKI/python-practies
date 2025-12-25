from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # 将数组转换为集合
        nums = set(nums)
        p = head

        # 我们主要关注头结点、尾结点
        while p != None:
            # 如果是头节点在集合中
            if id(head) == id(p) and p.val in nums:
                head = head.next
                p.next = None
                p = head
            # 如果是尾部结点的在集合
            elif p.next != None and p.next.next == None and p.next.val in nums:
                p.next = None
            # 如果不是头、尾的结点在集合中
            elif p.next != None and p.next.val in nums:
                p.next = p.next.next
            # 如果都不在集合中
            else:
                p = p.next

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
    s = Solution()
    head = array_to_nodes([1,2,1,2,1,2])
    res = s.modifiedList([1],head)
    print(f"移除节点之后的链表：{res}")


if __name__ == "__main__":
    main()