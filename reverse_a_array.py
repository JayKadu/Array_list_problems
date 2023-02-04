
def reverse(arr,start,end):
  while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1
arr=[1,2,4,5,6]
print("given: ",arr)
reverse(arr,0,len(arr)-1)
print("After reverse: ",arr)

#output:
# given: [1,2,4,5,6]
# After reverse: [6,5,4,2,1]


###
#Recursive Way

def reverseList(arr,start,end):
  while start>=end:
    return
  arr[start],arr[end]=arr[end],arr[start]
  reverseList(arr,start+1,end-1)

arr=[1,2,4,5,6]
print("given: ",arr)
reverseList(arr,0,len(arr)-1)
print("After reverse: ",arr)

#output:
# given: [1,2,4,5,6]
# After reverse: [6,5,4,2,1]



###
#Using slicing method

def reverse(arr):
  print("After reverse: ",arr[::-1])

arr=[1,2,4,5,6]
print("given: ",arr)
reverse(arr)

#output:
# given: [1,2,4,5,6]
# After reverse: [6,5,4,2,1]
  
  
  
  
