
def MAX_MIN(arr):
  print("MAX of array: ",max(arr))
  print("MIN of array: ",min(arr))
  
arr=[1,45,63,43,22,35,-12,98]
MAX_MIN(arr)


#output:
# MAX of array: 98
# MIN of array: -12


###
#using sorting method

def MAX_MIN(arr):
  arr.sort()
  print("MAX of array: ",arr[-1])
  print("MIN of array: ",arr[0])
  
arr=[1,45,63,43,22,35,-12,98]
MAX_MIN(arr)

#output:
# MAX of array: 98
# MIN of array: -12


###
#MAX and MIN using linear Search

class pair:
  def __init__(self):
    self.min=0
    self.max=0
    
def getmaxmin(arr:list,n:int) -> pair:
  minmax=pair()
    
  if n==1:
    minmax.max=arr[0]
    minmax.min=arr[0]
    return minmax
  if arr[0]>arr[1]:
    minmax.max=arr[0]
    minmax.min=arr[1]
  else:
    minmax.max=arr[1]
    minmax.min=arr[0]
    
  for i in range(2,n):
    if arr[i]>minmax.max:
      minmax.max=arr[i]
    elif arr[i]<minmax.min:
      minmax.min=arr[i]
        
  return minmax
  
if __name__=="__main__":
  arr=[1,45,63,43,22,35,-12,98]
  arr_size=8
  minmax=getmaxmin(arr,arr_size)
  print("MAX of array: ", minmax.max)
  print("MIN of array: ", minmax.min)
      
#output:
# MAX of array: 98
# MIN of array: -12
      
      
      
      
    
    
    
    
    
    
    







