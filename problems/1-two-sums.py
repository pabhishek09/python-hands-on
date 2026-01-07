# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List

def two_sums(nums: List[int], target: int) -> List[int]:
    for index in range(len(nums)):
        target_num = target-nums[index]
        try:
            target_index = nums.index(target_num)
            if  type(target_index) is int and target_index is not index :
                return [index, target_index]
        except ValueError:
            pass
    return []

print(two_sums([2,7,11,15], 26));