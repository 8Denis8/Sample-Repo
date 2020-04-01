a = [3, 5, 7, 0, 1]
#print(a[2])

fruits = ["apple", "mango", "cherry", "peach", "papaya"]
#print(fruits[2])
fruits.append("banana") #  metod APPEND - add to the end
#print(fruits)
fruits.insert(1, "orange") # meiod INSERT on specific index
#print(fruits)

fruits1 = fruits.copy();

fruits.remove("cherry") #  metod REMOVE by value
#print(fruits)
fruits.pop() # metod POP remove last
#print(fruits)
fruits.pop(1) # remove by index
#print(fruits)
length = len(fruits) # function LEN
#print(length)
fruits.append("apple")
#print(fruits.count("apple"))

# print(fruits1[:3])
# print(fruits1[1:3])
# print(fruits1[-1])
# print(fruits1[:-1])
# print(len(fruits1))
print(fruits1)
del fruits1[:2] # function DEL 