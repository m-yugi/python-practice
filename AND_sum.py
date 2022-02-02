a = [1,2,3,1]
l = len(a)
current = []
def find(index):
    global current
    if index == l:
        return
    else:
        find(index+1)
        current.append(a[index])
        print(current)
        find(index+1)
        current.pop()
print(find(0))