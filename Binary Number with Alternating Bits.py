# https://leetcode.com/problems/binary-number-with-alternating-bits/submissions/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        real_n=n
        status = True

        while n:
            if n==real_n:
                flag =n&1
            else:
                if flag!=n&1:
                    status = False
                    break
            flag = flag^1
            n>>=1
        return status
