# 17. Letter Combinations of a Phone Number

```yaml
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty: Medium
Topics:
  - Hash Table
  - String
  - Back Tracking
```

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

<img src="https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png" />
<br>

## Example 1:

```yaml
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

<br>

## Example 2:

```yaml
Input: digits = ""
Output: []
```

<br>

## Example 3:

```yaml
Input: digits = "2"
Output: ["a","b","c"]
```
 
<br>

## Constraints:

```yaml
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
```
