# Coding-Challenges
I would like to try out solutions to coding challenges I came across. Please let me know if you see better approch to same problem
1) Find 2 numbers from given array whose sum equals the target
  e.g. Input -> Target = 11 , array = [1,3,7,9,2]
       Output -> positions 3,4 (for numbers 9 and 2. Sum of 9 and 2 is 11)
2) Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
3) Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
4) Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.<a>https://leetcode.com/problems/backspace-string-compare/<a>
5) Longest substring we can form without repeating characters e.g. "abcbdca" - abc, cbd, bdca are substrings without repeating characters. Longest has length 4. <a>https://leetcode.com/problems/longest-substring-without-repeating-characters/<a>
6) Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
<a>https://leetcode.com/problems/reverse-linked-list-ii/<a>
7) Given are the 2 sorted arrays. Calculate median for cobmbined sorted array. 
Input 
a=[1,3,5]
b=[2,4,6]
Output
Median = 3.5
Combined array = [1, 2, 3, 4, 5, 6]
8) Serialize and deserialize binary tree. Make sure not to reconstruct tree again in deserialization process.. 
9) Largest product continuous subarray of integers.
10) Given a Roman numeral as input, your task is to find its corresponding integer value and output it. Roman Numerals are represented by combinations of letters from the Latin alphabet.
ALPHABET           VALUE
I                   1
V                   5
X                   10
L                   50
C                   100 
D                   500
M                   1000  
11) Move all 0s in array to the end.
e.g. 
Input: A[] = {1, 8, 3, 0, 2, 0, 1, 10, 13, 0}
Output: {1, 8, 3, 2, 1, 10, 13, 0, 0, 0}

-) You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own.
Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.
<a>https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/<a>