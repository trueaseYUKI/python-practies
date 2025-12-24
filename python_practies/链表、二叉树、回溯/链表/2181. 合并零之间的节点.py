from cmath import inf
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        temp = None
        p = head

        pre_sum = 0
        while p != None:
            # 如果指针指向的是0，并且不是头部
            if id(head) != id(p) and p.val == 0:
                node = ListNode(val=pre_sum)
                # 如果它接下来的值不是0
                if p.next != None and p.next.val != 0:
                    if ans == None:
                        ans = node
                        temp = ans
                    else:
                        temp.next = node
                        temp = temp.next
                if p.next == None:
                    if ans == None:
                        ans = node
                        temp = ans
                    else:
                        temp.next = node
                        temp = temp.next
                pre_sum = 0
            # 如果指针指向的不是0
            if p.val != 0:
                pre_sum += p.val

            p = p.next

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
    s = Solution()
    head = array_to_nodes([0,3,1,0,4,5,2,0])
    res = s.mergeNodes(head)
    print(f"合并后的结果：{res}")


if __name__ == "__main__":
    main()