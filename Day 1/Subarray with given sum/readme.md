# Solution

- Time Complexity: O(N)
- Auxiliary Space: O(1). Since no extra space has been taken. 

### The idea is simple as we know that all the elements in subarray are positive so, If a subarray has sum greater than the given sum then there is no possibility that adding elements to the current subarray will be equal to the given sum. So the Idea is to use a similar approach to a sliding window. 

- Start with an empty subarray 
- add elements to the subarray until the sum is less than x( given sum ). 
- If the sum is greater than x, remove elements from the start of the current subarray.

### Steps
- Create two variables, start=0, currentSum = arr[0]
- Traverse the array from index 1 to end.
- Update the variable currentSum by adding current element, currentSum = currentSum + arr[i]
- If the currentSum is greater than the given sum, update the variable currentSum as currentSum = currentSum - arr[start],
and update start as, start++.
- If the currentSum is equal to given sum, print the subarray and break the loop.


#### One more solution using setting up points
-  p
- [1 2 3 7 5]
-  p
-  Increase the pointer 2 until sum is not greater than required sum
-  If sum goes beyong required sum then decrease the previous (means pointer 1) by 1
-  again repeat the process until
-  sum become equal to the the required sum


        def subArraySum(arr, n, s)
            pnt1 = 0
            pnt2 = 0
            sum = arr[0]
            if(sum == s):
                return [1,1]

            while(pnt2 < n-1):
                if(sum + arr[pnt2+1] <= s):
                    sum += arr[pnt2+1]
                    pnt2+=1
                else:
                    sum -= arr[pnt1]
                    pnt1+=1
                if sum == s:
                    return [pnt1+1, pnt2+1]
            return [-1]
- Test Case

            arr = [1,2,3,7,5] 
            n = 5 
            sum = 12

            num = subArraySum(arr, n, sum) 
            for i in num:
                print(i)
