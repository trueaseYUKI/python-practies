from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans = 0
        p = head
        nums = set(nums)
        while p != None:
            if p.val in nums:
                if p.next == None:
                    ans += 1
                elif p.next.val not in nums:
                    ans += 1
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
    head = array_to_nodes([0,1,2,3,4])
    res = s.numComponents(head,[0,2,4])
    print(f"最长连续结点的个数：{res}")


if __name__ == "__main__":
    main()