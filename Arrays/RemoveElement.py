def remove_element(nums,val):
  i=0
  for j in range(0,len(nums)):
    if nums[j]!=val:
      nums[i]=nums[j]
      i+=1
  return nums[:i]

nums = [3, 2, 2, 3, 4, 2]
val = 2
result = remove_element(nums, val)
print("Modified array:", result)
