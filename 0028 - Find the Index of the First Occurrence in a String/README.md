# 28. Find the Index of the First Occurrence in a String


```yaml
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy
Topics:
  - Two Pointers
  - String
  - String Matching
```

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 
<br><br>

## Example 1:

```yaml
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

<br><br>

## Example 2:

```yaml
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```
 
<br><br>

## Constraints:

```yaml
- 1 <= haystack.length, needle.length <= 104
- haystack and needle consist of only lowercase English characters.
```
