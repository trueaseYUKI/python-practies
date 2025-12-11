from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        if len(arr) == 1:
            if (arr[0] / k) >= threshold:
                return 1
            else:
                return 0

        cnt = 0
        sum = 0
        # 1.先找出第一个子数组是否大于阈值
        for i in range(0,k):
            sum += arr[i]

        if (sum / k) >= threshold:
            cnt += 1

        for i in range(k,len(arr)):
            sum += arr[i]
            sum -= arr[i - k]
            average = sum / k

            if average >= threshold:
                cnt+=1

        return cnt




class main():
    print(Solution().numOfSubarrays([2,2,2,2,5,5,5,8],3,4))
    pass

if __name__ == "__main__":
    main()