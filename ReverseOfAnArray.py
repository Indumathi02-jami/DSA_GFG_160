class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        left = 0
        right = n-1
        while(left<=right):
            temp = arr[left]
            arr[left]=arr[right]
            arr[right] = temp
            left=left+1
            right = right-1
        