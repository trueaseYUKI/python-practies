# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = [-1,-1]
        pos_index = []

        temp = head
        pre = head.val
        pos = 0

        # 先记录下每个临界点的位置
        while temp != None:
            pos += 1
            if temp.next != None and id(temp) != id(head):
                next_node = temp.next
                if pre < temp.val > next_node.val or pre > temp.val < next_node.val:
                    pos_index.append(pos)
                pre = temp.val
            temp = temp.next

        # 再计算最大、最小的临界点距离
        n = len(pos_index)
        # 如果有两个及以上的临界点
        if n > 1:
            ans[1] = pos_index[n-1] - pos_index[0]
            for i in range(0,n):
                if ans[0] == -1:
                    ans[0] = pos_index[i+1] - pos_index[i]
                elif i + 1 < n:
                    temp = pos_index[i + 1] - pos_index[i]
                    ans[0] = min(ans[0],temp)

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
    head = array_to_nodes([6,8,4,1,9,6,6,10,6])
    res = s.nodesBetweenCriticalPoints(head)
    print(f"最小和最大距离：{res}")


if __name__ == "__main__":
    main()