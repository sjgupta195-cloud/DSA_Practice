# count sum of pair equals = 7

nums = [1, 2, 3, 4, 5, 6]

left = 0
right = len(nums)-1

count = 0
 
while left < right :
    if nums[left] + nums[right] == 7 :
        count += 1

    left += 1
    right -= 1
    
print (count)



      
