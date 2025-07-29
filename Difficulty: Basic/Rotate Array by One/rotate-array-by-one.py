#User function Template for python3

class Solution:
    def rotate(self, arr):
        arr.insert(0, arr.pop())
        return arr