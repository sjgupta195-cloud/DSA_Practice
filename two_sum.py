nums = [2, 7, 11, 15]
target = 9

seen = {}

for num in nums :
    
    complement = target - num 

    if complement in seen :
        print ("Found :", complement, num)
        break 

    seen[num] = True