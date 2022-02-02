n=int(input())
l=list(map(int,input().split(" ")))
for i in range(len(l)):
    l[i]=l[i]*l[i]
l.sort();
for i in l:
    print(i)