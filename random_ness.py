from collections import deque


def printPowerSet(S, i, out=deque()):
    if i < 0:
        print(*list(out))
        return
    out.append(S[i])
    printPowerSet(S, i - 1, out)
    out.pop()
    while i > 0 and S[i] == S[i - 1]:
        i = i - 1
    printPowerSet(S, i - 1, out)


def findPowerSet(S):
    S.sort()
    printPowerSet(S, len(S) - 1)


if __name__ == '__main__':
    s = []
    for i in range(int(input())):
        s.append(int(input()))
    findPowerSet(s)
