class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:]
        for i in range(32 - len(b)):
            b = '0' + b
        return int(b[::-1], 2)

    def reverseBitsMani(self, n):
        ans = 0
        for i in xrange(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans
