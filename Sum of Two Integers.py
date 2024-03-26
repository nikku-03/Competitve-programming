class Solution(object):
  def getSum(self, a, b):
    if b == 0:
      return a
    sum = a ^ b
    carry = (a & b) << 1
    return self.getSum(sum, carry)
