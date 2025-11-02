class Solution:
    def inversionCount(self, arr):
        # Code Here
        return self.countIn(arr,0, len(arr)-1);
    
    def countIn(self,arr, l , r):
        res=0
        if(l>=r):
            return 0
        mid = (l+r) // 2
            
        res+=self.countIn(arr,l,mid)
        res+=self.countIn(arr,mid+1,r)
            
        res+=self.merge(arr,l,r,mid)
            
        return res
            
    def merge(self,arr, l, r, m):
        n1 = m-l+1
        n2 = r-m
        
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        
        re=0
        i=0
        j=0
        k=l
        
        while i<n1 and j<n2:
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
                re += (n1-i)
            k+=1
            
        while i<n1:
            arr[k]=left[i]
            i+=1
            k+=1
            
        while j<n2:
            arr[k]=right[j]
            j+=1
            k+=1
            
        return re
                
        
            
        
        