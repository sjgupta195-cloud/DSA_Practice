# to find largest number in array 

nums = [10, 25, 30, 40, 55, 65]

largest = nums[0]

for num in nums :
    if num > largest:
        largest = num

print (largest)

# to find total sum of array

total = 0

for num in nums :
    total += num

print (total)

# for even numbers 

count = 0

for num in nums :
    if num % 2 == 0 :
        count += 1
       
print (count)         

# find the largest even number 

even_largest = nums[0]

for num in nums :
    if num % 2 == 0:
        if num > even_largest:
            even_largest = num

print (even_largest)

# count number grater than 25 

count_big = 0

for num in nums :
    if num > 25 :
        count_big += 1

print (count_big)