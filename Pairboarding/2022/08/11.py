# reverse list
# Write a function, reverseList, that takes in the head of a linked list as an argument.
# The function should reverse the order of the nodes in the linked list in-place
# and return the new head of the reversed linked list.

# const reverseList = (head) => {}

"""
declare previous node, set to None
declare current node, set to head
iterate through the list
    at each node
        save next as temp maybe
        set its .next to previous node
        set current node to previous node
        set next to current

return previous
"""

def reverseList(head):
    prev = None
    curr = head

    while curr:
        curr.next, curr, prev = prev, curr.next, curr

    return prev

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        curr = self
        a = []
        while curr:
            a.append(curr.val)
            curr = curr.next
        return (", ").join(a)

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')1
# a.next = b2
# b.next = c
# c.next = d
# d.next = e
# e.next = f # a -> b -> c -> d -> e -> f
# print(reverseList(a)) # f -> e -> d -> c -> b -> a

# x = Node('x')
# y = Node('y')
# x.next = y
# print(reverseList(x)) # y -> x

# p = Node('p') # p
# print(reverseList(p)) # p




# Say that I gave you an array of length n, containing the numbers 1..n in
# jumbled order. "Sort" this array in O(n) time. You should be able to do
# this without looking at the input.

# [1,4,2,5,3] => [1,2,3,4,5]