d={x: nums.count(x) for x in nums}
lkey=list(d.keys())
lval=list(d.values())
print(lkey[lval.index(1)])