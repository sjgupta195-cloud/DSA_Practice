# palindrome problem 

word = "madam"

left = 0
right = len(word) - 1

while left < right :
    if word[left] != word[right]:
        print ("Not a Palindrome")
        break
        
    left += 1
    right -=1

else :
        
    if left >= right :
        print ("It is a Palindrome")


