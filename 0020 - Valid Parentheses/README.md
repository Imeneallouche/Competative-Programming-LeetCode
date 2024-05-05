# 20. Valid Parentheses

```yaml
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Topics:
  - String
  - Stack
```

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

<br>

## Example 1:

```yaml
Input: s = "()"
Output: true
```

<br>

## Example 2:

```yaml
Input: s = "()[]{}"
Output: true
```

<br>

## Example 3:

```yaml
Input: s = "(]"
Output: false
```

<br>

## Constraints:

```yaml
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
```
