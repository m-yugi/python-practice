def combinationSum(candidates, target):
    return getAllSolutions(candidates, 0, target, [])
def getAllSolutions(candidates, s, target, curr):
    allSolutions = []
    SUM=1
    for i in curr:
        SUM*=i        
    for n in range(s, len(candidates)):
        currsum = SUM * candidates[n]
            
        if currsum < target:
            allSolutions.extend(getAllSolutions(candidates, n, target, curr + [candidates[n]]))
        elif currsum == target:
            allSolutions.extend([curr + [candidates[n]]])
            
    return allSolutions
inarr=list(map(int,input().split()));
innum=int(input())
l=combinationSum(inarr,innum)
print(l)