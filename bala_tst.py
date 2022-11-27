def f(s):
     d = {}
    res = ""
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i, v in d.items():
        if(v >= 2):
            if(res == ""):
                res = i
            else:
                return "0"
    return res


print(f("a string"))