for i in range(int(input())):
    n = int(input())
    s = input()
    ans = True
    while(n > 0):
        mid = (n//2)
        if(n % 2 != 0):
            n -= 1
        else:
            if(s[0:mid] == s[mid:n]):
                n //= 2
            else:
                ans = False
                break
    if(ans):
        print("YES")
    else:
        print("NO")
