#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
       #Write your code here
        curr_sum = arr[0] 
        start = 0
        sum = s
        i = 1
        while i <= n: 
              
            while curr_sum > sum and start < i-1: 
              
                curr_sum = curr_sum - arr[start] 
                start += 1
                  
            if curr_sum == sum:
                return [start+1, i]
      
            if i < n: 
                curr_sum = curr_sum + arr[i] 
            i += 1
      
        return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends


# --------------------------------- Test Cases
# arr = [1,2,3,7,5] 
# n = 5 
# sum = 23
  
# num = subArraySum(arr, n, sum) 
# for i in num:
#     print(i)
