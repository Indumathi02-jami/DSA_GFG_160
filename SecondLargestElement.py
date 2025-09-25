class Solution:
    def getSecondLargest(self, arr):
        lar=-1
        sec=-1
        n=len(arr)
        for i in range(0,n):
            if(lar<arr[i]):
                sec=lar
                lar=arr[i]
            elif arr[i]<lar and arr[i]>sec:
                sec=arr[i]
        return sec