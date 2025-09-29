class Solution:
    def missingNumber(self, arr):
        # code here
        n=len(arr)
        for i in range(1,n+2):
            if i not in arr:
                return i
                break