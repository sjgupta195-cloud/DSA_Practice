# duplicates

nums =(1, 1, 2, 3, 3, 3, 4, 4 )

frequency = {}

for num in nums :

    if num not in frequency :
        frequency[num] = 1

    else :
        frequency[num] += 1

print (frequency)
