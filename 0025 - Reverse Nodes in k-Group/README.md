# 25. Reverse Nodes in k-Group

```yaml
Link: hthttps://leetcode.com/problems/reverse-nodes-in-k-group/
Difficulty: Hard
Topics:
  - Recursion
  - Linked List
```

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


<br>

# Example 1:

```yaml
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

<br>

# Example 2:

```yaml
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```



<br>

# Constraints:

```yaml
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
```
