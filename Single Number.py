class Solution(object):
  def singleNumber(self, nums):
    if len(nums) == 0:
      return None
    elif len(nums) == 1:
      return nums[0]
    else:
      xor_prod = 0
      for entries in nums:
        xor_prod ^= entries
      return xor_prod
