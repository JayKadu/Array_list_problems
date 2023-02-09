#Move all negative numbers to beginning and positive to end with constant extra space

def move(arr):
  arr.sort()
  
arr=[ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
move(arr)
for i in arr:
  print(i, end=" ")
  
#output: -7 -3 -1 2 4 5 6 8 9 

  
  
  
###using quick sort
  
def rearrange(arr):
  
  n=len(arr)
  j=0
  for i in range(0,n):
    if (arr[i]<0):
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp
      j=j+1
  print(arr)
  
arr=[ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
rearrange(arr)

#output: [-1, -3, -7, 4, 5, 6, 8, 9]
    
    
