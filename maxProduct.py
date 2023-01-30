#finding the maximum product in an list

def maxProduct(arr):
  maxProduct=0
  for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i]* arr[j]>maxProduct:
        maxProduct= arr[i]*arr[j]
        pairs=str(arr[i])+"," str(arr[j])
  print(pairs)
  print(maxProduct)
  
maxProduct([1,20,30,44,5,34,78,90,89,97,76])

#output: 97,90
#        8730
