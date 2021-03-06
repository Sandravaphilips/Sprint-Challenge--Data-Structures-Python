import time
from binary_search_tree import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
bts = BinarySearchTree(names_1[0])
for i in names_1[1:]:
    bts.insert(i)
    
for i in names_2:
    if bts.contains(i):
        duplicates.append(i)
# res = filter(lambda x: x in names_1, names_2)
# duplicates = list(res)

# index = 0
# while index < 10000:
#     if names_1[index] in names_2:
#         duplicates.append(names_1[index])
#     index += 1

# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
