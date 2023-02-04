
def kthSmallestElement(arr,k):
  arr.sort()
  print(arr[k-1])
  
arr=[7,10,4,3,20,15]
kthSmallestElement(arr,3)

#output: 7


###
#kth smallest element of unsorted array using binary search

import sys

def count(nums,mid):
  cnt=0
  for i in range(len(nums)):
    if nums[i]<=mid:
      cnt+=1
  return cnt

def kthsmallest(nums,k):
  low=sys.maxsize
  high=-sys.maxsize-1
  
  for i in range(len(nums)):
    low=min(low,nums[i])
    high=max(high,nums[i])
    
  while low<high:
    mid=low+(high-low)//2
    
    if count(nums,mid)<k:
      low=mid+1
    else:
      high=mid
  return low

if __name__ == "__main__":
    nums = [7,10,4,3,20,15]
    k = 3
    
    print("Kthsmallestelement: ", kthsmallest(nums, k))

#output: 
# Kthsmallestelement: 7
    
    
    
    
    
    
  
