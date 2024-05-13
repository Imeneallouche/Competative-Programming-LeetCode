# 41. First Missing Positive

```yaml
Link: https://leetcode.com/problems/first-missing-positive/
Difficulty: Hard
Topics:
  - Array
  - Hash Table
```

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

<br>

## Example 1:

```yaml
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
```

<br>

## Example 2:

```yaml
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
```

<br>

## Example 3:

```yaml
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
```

<br>

## Constraints:

```yaml
1 <= nums.length <= 105
-2**31 <= nums[i] <= 2**31 - 1
```
