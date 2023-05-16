class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

def check_power_of_three(n):
    sol = Solution()
    is_power_of_three = sol.isPowerOfThree(n)
    if is_power_of_three:
        print("{} is a power of three.".format(n))
    else:
        print("{} is not a power of three.".format(n))

# Usage
check_power_of_three(32)
