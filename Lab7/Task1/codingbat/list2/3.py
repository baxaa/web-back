def centered_average(nums):
  sum = 0
  for element in nums:
    sum += element
  return (sum - min(nums) - max(nums)) / (len(nums)-2) 