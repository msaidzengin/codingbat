"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""

def sum67(nums):
  count = 0
  flag = 0
  for n in nums:
    if n == 6:
      flag = 1
      continue
    if flag and n == 7:
      flag = 0
      continue
    if not flag:  
      count += n
  
  return count
