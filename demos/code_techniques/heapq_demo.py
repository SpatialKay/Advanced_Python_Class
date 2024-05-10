import heapq

# heapq is a module in Python that provides a collection of heap queue
# algorithms. It allows you to efficiently manipulate and maintain a
# heap data structure, which is a specialized tree-based structure that
# satisfies the heap property (either min-heap or max-heap).

# A min-heap and a max-heap are both specialized forms of binary heap data
# structures used in computer science and data processing for efficient
# management of elements with respect to their values. They are often used
# in priority queues, heapsort, and various other algorithms.

# Here are the key differences between a min-heap and a max-heap:

# **Min-Heap:**
# 1. In a min-heap, the value of each node (including the root) is less than
# or equal to the values of its children.
# 2. The smallest element is at the root of the heap, which makes it suitable
# for finding the minimum element quickly.
# 3. Min-heaps are used in algorithms where you need to extract the smallest
# element efficiently, such as Dijkstra's algorithm for finding the shortest
# path in a graph.

# **Max-Heap:**
# 1. In a max-heap, the value of each node (including the root) is greater
# than or equal to the values of its children.
# 2. The largest element is at the root of the heap, which makes it suitable
# for finding the maximum element quickly.
# 3. Max-heaps are used in algorithms where you need to extract the largest
# element efficiently, such as heapsort, which is an in-place sorting
# algorithm.

# Both min-heaps and max-heaps are typically implemented as binary trees,
# with the heap property enforced such that the parent node's value is
# compared with its children in a way that maintains the desired ordering
# (minimum or maximum).

# Here's a visual representation of a min-heap and a max-heap:

# **Min-Heap:**

# ```
#      1
#     / \
#    2   3
#   / \ / \
#  4  5 6  7
# ```

# **Max-Heap:**

# ```
#      7
#     / \
#    5   6
#   / \ / \
#  2  4 3  1
# ```

# In summary, min-heaps and max-heaps are used for maintaining ordered
# collections of elements, with the primary difference being the order
# in which elements are organized. Min-heaps prioritize smaller elements,
# while max-heaps prioritize larger elements.

# Create an empty list to represent a min-heap
min_heap = []

# Insert elements into the min-heap
elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for element in elements:
    heapq.heappush(min_heap, element)

print("Min-Heap after inserting elements:", min_heap)

# Get the smallest element (root of the min-heap)
smallest = heapq.heappop(min_heap)
print("Smallest element:", smallest)

# Insert a new element into the min-heap
new_element = 0
heapq.heappush(min_heap, new_element)
print("Min-Heap after inserting", new_element, ":", min_heap)

# Find the smallest element without removing it
smallest = heapq.heappop(min_heap)
print("Smallest element (without removal):", smallest)

# Convert a list into a valid min-heap in-place
unordered_list = [7, 8, 2, 3, 1]
heapq.heapify(unordered_list)
print("Min-Heap created from an unordered list:", unordered_list)

# Find the n largest elements in a list using nlargest
n_largest = heapq.nlargest(3, elements)
print("3 largest elements:", n_largest)

# Find the n smallest elements in a list using nsmallest
n_smallest = heapq.nsmallest(3, elements)
print("3 largest elements:", n_smallest)
