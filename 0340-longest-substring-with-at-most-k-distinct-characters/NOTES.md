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
If we have already found a window of length max_size, then what we need to do next is to search for a larger valid window, for example, a window with length max_size + 1. Therefore, in the following sliding window process, even if the current window with size max_size is not valid, there is no problem, because we have already found a window of length max_size before, so we may as well continue looking for a larger window.
​
​
Understanding this, we can simplify the solution in approach 2:
​
Again, we use a hash map counter to keep track of the frequency of each letter in the current window. When we increase the window length by 1, we need to increase the count of the character at the current right boundary counter[s[right]] by 1.
​
img
​
If the expanded window is still valid, it means that we get a larger valid window with length max_size + 1 (from 2 to 3). We can continue to move the boundary right.
​
img img
​
However, if the expanded window is invalid, we only need to remove the leftmost character in the window to keep the window length still at max_size (from 4 to 3), that is, decrease counter[s[right - max_size]] by 1.
​
Similiarly, we delete the key s[i] from counter if counter[s[i]] = 0.
​
img
​
Since the expanded window of length 4 was invalid, we removed a character from the leftmost side of the window to make its length 3 again. Although the current window is still invalid, we don't need to keep shrinking it because we have previously found a valid window of length 3. We can continue to shift the boundary right to try the next window of size 4.
​
img
​
Once this iteration is over, max_size represents the maximum size of the valid window.