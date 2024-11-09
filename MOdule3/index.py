#my_set = {1,2,3}
from enum import unique

#print(my_set)
#
# my_set = ([4,5,6])
# print(my_set)
#
# my_set = set()
# print(my_set)

my_set = {1,1,2,3,3,4,5,3,2,3}
print(my_set)

#####

set1 = {1,2,3}
set_2 = {3,4,5}


union_method = set1.union(set_2)

union_operator = set1 | set_2

print("Union of set1 and set2 using method:", union_method)

print("Union of set1 and set2 using operator", union_operator)

#Compute intersection between set1 and set2 using the interactions method

intersection_method = set1.intersection(set_2)

intersection_operator = set1 & set_2

print("Intersection of set1 and set2 using the intersection method", intersection_method)
print("Intersection of set1 and set2 using the intersection operator", intersection_operator)

difference_method = set1.difference(set_2)

difference_operator = set1 - set_2

print("Difference of set1 and set2 using the difference method", difference_method)
print("Difference of set1 and set2 using the difference operator", difference_operator)

symmetric_difference_method = set1.symmetric_difference(set_2)
symmetric_difference_operator = set1 ^ set_2

print("Symmetric difference of set1 and set2 using symmetric difference method", symmetric_difference_method)
print("Symmetric difference of set1 and set2 using symmetric difference operator", symmetric_difference_operator)


my_set = {1,2,3}

my_set.add(7)

my_set.remove(3)

my_set.discard(8)
print(my_set)

my_set.clear()

print(my_set)

my_list = [1,2,2,2,3,4,4,4,5,6]

unique_set = set(my_list)

print(unique_set)

unique_list = list(unique_set)

print(unique_list)



gentrit_interest = {"music", "movies","travel"}
eris_interest = {"movies", "games" , "skiing"}

common_interest = gentrit_interest.intersection(eris_interest)
print(common_interest)

colors = {"red", "green" , "yellow", "blue"}
color = "blue"
print(color in colors)


