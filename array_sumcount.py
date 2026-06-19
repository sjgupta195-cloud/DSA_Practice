nums = [1, 2, 3, 4, 5, 6, 7, 8]

left = 0
right = len(nums)-1

new_count = 0

while left < right :

    current_sum = nums[left] + nums[right]
    
    if current_sum == 9 :
        new_count += 1
        
        left += 1
        right -= 1

    elif current_sum < 9  :
        
        left += 1 
    else :
        right -=1 
        

print (new_count)
      
