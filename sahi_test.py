def hello(friend, time) -> list[int]:
    start = end = 0
    if(friend > time):
        return [time, time+1]
    elif(time-friend == 1):
        return [friend-1, friend-2]
    elif(time % friend == 0):
        if((time//friend) % 2 == 0):
            return [friend, 0]
        else:
            return [friend-1, friend]
    else:
        if((time//friend) % 2 != 0):
            end = friend-(time % friend)
            start = end+1
        else:
            start = (time % friend)
            end = start+1
    return [start, end]


print(*hello(3, 9))
