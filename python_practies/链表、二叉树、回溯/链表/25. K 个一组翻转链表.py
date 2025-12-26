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


        return head



def main():
    head = array_to_nodes([1,2,3,4,5])
    s = Solution()
    res = s.reverseKGroup(head,2)
    print(f"反转后的链表：{res}")

if __name__ == "__main__":
    main()