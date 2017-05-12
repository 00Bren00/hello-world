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

nums = [1, 2, 3]
nums.append(4)
print(nums)
#can append items to the end of a list

nums = [1, 3, 5, 2, 4]
print(len(nums))#5
#len function gets the num of items in a list

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)#['Python', 'is', 'fun']
#insert adds items at a specific index

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))
#The index method finds the first occurrence of a list item and returns its index.
#If the item isn't in the list, it raises a ValueError.
#There are a few more useful functions and methods for lists.
#max(list): Returns the list item with the maximum value
#min(list): Returns the list item with minimum value
#list.count(obj): Returns a count of how many times an item occurs in a list
#list.remove(obj): Removes an object from a list
#list.reverse(): Reverses objects in a list