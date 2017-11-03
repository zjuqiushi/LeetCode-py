A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if(len(A) < 3): 
            return 0
        cnt = 2
        ans = 0
        l = []
        d = A[1] - A[0]
        for i in range(2,len(A)):
            if(A[i] - A[i-1] == d): 
                cnt+=1
            else:
                if cnt >= 3:
                    l.append(cnt)
                cnt = 2
                d = A[i] - A[i-1]
        if cnt >= 3:
            l.append(cnt)
        for i in l:
            ans += (i-1)*(i-2)/2
        return ans

    
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        dp = []
        for i in range(0,size):
            dp.append(0)
        if(size < 3):
            return 0
        if(A[2]-A[1] == A[1]-A[0]):
            dp[2] = 1
        ans = dp[2]
        d = A[2]-A[1]
        for i in range(3,size):
            if(A[i]-A[i-1] == d):
                dp[i] = dp[i-1] + 1
                ans += dp[i]
            else:
                d = A[i] - A[i-1]
        return ans
