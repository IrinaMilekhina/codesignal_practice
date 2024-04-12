"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List

n_1 = [2, 7, 11, 15]
t_1 = 9
n_2 = [3, 2, 4]
t_2 = 6
n_3 = [3, 3]
t_3 = 6
n_4 = [1, 0, 10, -10]
t_4 = 10
n_5 = [-1, -2, -3, -4, -5]
t_5 = -8


def find_terms(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, el in enumerate(nums):
        if not nums_map.get(el):
            nums_map[el] = [i, ]
        else:
            nums_map[el].append(i)
    s_nums = sorted(nums)
    first_i = 0
    last_i = len(s_nums) - 1
    if target < 0:
        while s_nums[first_i] < target:
            first_i += 1
    else:
        while s_nums[last_i] > target:
            last_i -= 1
    curr_sum = s_nums[first_i] + s_nums[last_i]
    while curr_sum != target:
        if curr_sum < target:
            first_i += 1
        else:
            last_i -= 1
        curr_sum = s_nums[first_i] + s_nums[last_i]
    result = [nums_map[s_nums[first_i]].pop(), nums_map[s_nums[last_i]].pop()]
    return result


print(find_terms(n_1, t_1))  # [0,1]
print(find_terms(n_2, t_2))  # [1,2]
print(find_terms(n_3, t_3))  # [0,1]
print(find_terms(n_4, t_4))  # [1,2]
print(find_terms(n_5, t_5))  # [2,4]
