str = "Hello world!"
print(str[6])#w

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)#can add and multiply lists like strings

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)# checks to see if the item is in the list
#true true false
#The in operator is also used to determine whether or not
#  a string is a substring of another string.

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
#can combine not with in
