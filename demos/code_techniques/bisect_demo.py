import bisect

# The bisect module in Python provides functions to perform binary searches
# on sorted sequences. It allows you to efficiently find the insertion point
# for a new element in a sorted list or to locate an element in a sorted
# list.

# Sorted list of numbers
sorted_list = [1, 3, 5, 7, 9]

# Inserting an element while maintaining the sorted order
element_to_insert = 4
index_to_insert = bisect.bisect(sorted_list, element_to_insert)
sorted_list.insert(index_to_insert, element_to_insert)
print("List after inserting 4:", sorted_list)  # Output: [1, 3, 4, 5, 7, 9]

# Finding the insertion point for a new element
new_element = 6
insertion_point = bisect.bisect(sorted_list, new_element)
print(f"Insert {new_element} at index {insertion_point} to maintain sorting.")

# Using insort to insert an element while maintaining the sorted order
bisect.insort(sorted_list, 2)

# Output: [1, 2, 3, 4, 5, 7, 9]
print("List after inserting 2 using insort:", sorted_list)

# Finding an element's position in the sorted list
element_to_find = 5
position = bisect.bisect_left(sorted_list, element_to_find)
if sorted_list[position] == element_to_find:
    print(f"{element_to_find} found at index {position}.")
else:
    print(f"{element_to_find} not found in the list.")
