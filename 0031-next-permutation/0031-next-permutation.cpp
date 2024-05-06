class Solution {
public:
   void nextPermutation(vector<int>& arr) {
        int n = arr.size();
        int i = n-1;
        int j = i-1;
        int pv = 0;
        int inp = 0;
        int flag = 0;
        while(i>0){
            if(arr[i]>arr[j]) {
                pv = arr[j];
                inp = j;
                flag = 1;
                break;
            }
            i--;
            j--;
        }
        if(flag == 0){
            sort(arr.begin(),arr.end());
            return;
        }
        
     
        int in ;
        for(int k = n-1;k>inp;k--){
            if(arr[k]>arr[inp]){
                   in = k;
                   break;
            }
        }
        swap (arr[in],arr[inp]);
       reverse(arr.begin() + inp + 1 , arr.end());
        
    }
};