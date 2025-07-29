class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        self.arr=arr
        a=list(set(self.arr))
        a.sort()
        if(len(a)==1):
            return -1
        elif(len(a)==0):
            return 0
        else:
            return a[-2]