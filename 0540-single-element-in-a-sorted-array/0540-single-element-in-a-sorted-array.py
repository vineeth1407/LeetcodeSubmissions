class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        if not arr:
            return None
        if len(arr)==1:
            return arr[0]
        
        if arr[0]!=arr[1]:
            return arr[0]

        n = len(arr)
        if arr[n-1]!=arr[n-2]:
            return arr[n-1]
        
        low = 1
        high = n-2

        while low<=high:
            mid = (low+high)//2
            if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
                return arr[mid]
            if (mid%2==0 and arr[mid]==arr[mid+1]) or (mid%2!=0 and arr[mid]==arr[mid-1]):
                low = mid+1
            else:
                high = mid-1
        #Idea is to check the equal element position , on left of single element
        # for odd index, equal element will be on even
        # for even index equal element will be on odd
        # on the right of single element it will be viceversa
        return -1
        