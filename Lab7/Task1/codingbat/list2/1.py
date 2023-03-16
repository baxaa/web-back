def count_evens(nums):
  count = 0
  for element in nums:
    if element % 2 == 0:
      count += 1
  return count