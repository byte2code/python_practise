#Solution

- Create two variables, start=0, currentSum = arr[0]
- Traverse the array from index 1 to end.
- Update the variable currentSum by adding current element, currentSum = currentSum + arr[i]
- If the currentSum is greater than the given sum, update the variable currentSum as currentSum = currentSum - arr[start],
and update start as, start++.
- If the currentSum is equal to given sum, print the subarray and break the loop.
