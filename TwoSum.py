#Find pairs which is equal to target

def findpairs(mylist,target):
  a=[]
  for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
      if mylist[i]==mylist[j]:
        continue
      elif mylist[i]+mylist[j]==target:
        a.append([i,j])
  print(a)

findpaires([2,7,11,15],9)

#output: [[0,1]]
# O(N*N)
    
    
