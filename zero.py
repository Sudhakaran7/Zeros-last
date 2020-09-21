n=int(input())
arr=list(map(int,input().split()))
count=0
res=[]
for i in range(len(arr)):
  if(arr[i]==0):
    count+=1
  else:
    res.append(arr[i])
for j in range(count):
  res.append(0)
print(*res)
