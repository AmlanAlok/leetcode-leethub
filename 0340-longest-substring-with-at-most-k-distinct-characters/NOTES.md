Approach 2: Sliding Window
Intuition
We can also find the longest valid window with fewer traversals. Unlike the previous fixed-length sliding window solution, this time we can adjust the window length based on the situation. We will still use the counter counter to record the counter of each type of character within the window.
​
Specifically, if the current window is valid, we can try to expand the window by moving the right boundary one position to the right, right = right + 1. On the other hand, if the current window is invalid, we keep moving the left boundary to the right (equivalent to removing the leftmost character from the window) until the window becomes valid, that is left = left + 1. During this process, we constantly record the longest valid window seen so far.
​
As shown in the following figure, we keep adjusting the size of the window and recording the maximum size of the valid window.
​
Approach 3: Sliding Window II
Intuition
In the previous solution, we need to ensure that the current window is always valid. If the window contains more than k distinct characters, we need to continuously remove the leftmost character in the window. During this process, the size of the window may decrease, even smaller than the previous valid window. Taking the figure below as an example, the window on the left is valid, but the window' on the right is not valid, and we need to remove the left characters from it to make it valid.
​
img
​
​
However, we don't need to decrease the size of the window.
​
img