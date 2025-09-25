
class Solution {
    void pushZerosToEnd(int[] arr) {
        // code here
        int n=arr.length;
        int in=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]!=0){
                arr[in++]=arr[i];
            }
        }
        while(in<n){
            arr[in++]=0;
        }
    
    }
}