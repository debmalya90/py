#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	
    	n=len(arr)
    	lnz=0
    	for i in range(n):
    	    if arr[i]!=0:
    	        arr[lnz], arr[i]=arr[i], arr[lnz]
    	        lnz+=1
        return arr