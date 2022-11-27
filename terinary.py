# convert decimal to ternary
def mathchallenge(num):
    s = ""
    if(num <= 2):
        return num
    while(num > 0):
        rem = num % 3
        num = num//3
        s = str(rem) + s
    num = int(s)
    return num
print(mathchallenge(int(input())))