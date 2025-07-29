class Solution:
    def largest(self, arr):
        # code here
        self.arr=arr
        a=list(set(self.arr))
        a.sort()
        return a[-1]
        
