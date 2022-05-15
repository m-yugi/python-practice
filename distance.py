from pydoc import Helper


store={}
n=int(input())
cost=0 
def helper(i,num,arr):
    if arr[i] not in store:
        return
    else:
arr=[int(input()) for i in range(n)]
num=[int(input()) for i in range(n)]
for i in range(n):
    if arr[i] in store:
        helper(i,num,arr)
    else:
        store[arr[i]]=i