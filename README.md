# 🧮 Day 26: Non-overlapping Intervals – GFG 160 Days DSA Challenge

## 📘 Problem Statement:
You're given a 2D array `intervals[][]` where `intervals[i] = [starti, endi]`.  
Your task is to **remove the minimum number of intervals** so that the remaining intervals do **not overlap**.

📌 An interval `[a, b]` overlaps with `[c, d]` if `a < d` and `c < b`.

---

## 🧠 Approach:
Sort the intervals based on their end time. Why? Because choosing intervals with earlier end times leaves room for more future intervals.

Iterate through the intervals:

If the current interval starts after or at the end of the previous interval, it's non-overlapping.

Count such valid (non-overlapping) intervals.

Final answer = Total Intervals - Count of Non-overlapping Intervals

---

## ⏱ Time & Space Complexity:
Time: O(N log N) – due to sorting

Space: O(1) – constant extra space used

---

## 💡 What I Learned:
This was a classic greedy problem disguised as interval deletion. Sorting strategically helped reduce the problem to a single pass count. It was a good exercise in minimizing removals by maximizing valid intervals.

---

## 🚀 Challenge Track:
#gfg160 #geekstreak2025
