from typing import Optional, List
from math import floor
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

def sum_reverse_linked_list(l1: List[int], l2: List[int]) -> List[int]:

    def get_number_from_linked_list(l):
        print(f"Get number for {l}")
        num = 0
        for index in range(len(l)):
            num += l[index] * (10**index)
        return num
    sum = get_number_from_linked_list(l1)+ get_number_from_linked_list(l2)
    sum_list=[]
    while(sum > 0):
        sum_list.append(sum % 10)
        sum = floor(sum / 10)
    return sum_list

print(sum_reverse_linked_list([2,4,3], [5,6,4]))