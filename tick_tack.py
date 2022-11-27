list1 = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
p1 = input("please enter the name of the first player :")
print("\n")
p2 = input("please enter the name of the second player :")
print("\n")
turns = 1
flag = False
while(turns <= 9):
    if(turns % 2 == 0):
        while(True):
            pos1 = int(input(p1+" please enter the position of O :"))-1
            if(list1[pos1] == "_"):
                list1[pos1] = "O"
                break
            else:
                print("position is already marked please enter again")
    else:
        while(True):
            pos2 = int(input(p2+" please enter the position of X :"))-1
            if(list1[pos2] == "_"):
                list1[pos2] = "X"
                break
            else:
                print("position is already marked please enter again")
    print("After ", turns)
    print(list1[0], " | ", list1[1], " | ", list1[2])
    print(list1[3], " | ", list1[4], " | ", list1[5])
    print(list1[6], " | ", list1[7], " | ", list1[8])
    print("\n")
    if list1[0] == list1[1] == list1[2] == "O":
        print(p1+" is the winner")
        flag = True
        break
    elif list1[0] == list1[1] == list1[2] == "X":
        print(p2+" is the winner")
        flag = True
        break
    elif list1[3] == list1[4] == list1[5] == "O":
        print(p1+" is the winner")
        flag = True
        break
    elif list1[3] == list1[4] == list1[5] == "X":
        print(p2+" is the winner")
        flag = True
        break
    elif list1[6] == list1[7] == list1[8] == "O":
        print(p1+" is the winner")
        flag = True
        break
    elif list1[6] == list1[7] == list1[8] == "X":
        print(p2+" is the winner")
        flag = True
        break
    elif list1[0] == list1[4] == list1[8] == "O":
        print(p1+" is the winner")
        flag = True
        break
    elif list1[0] == list1[4] == list1[8] == "X":
        print(p2+" is the winner")
        flag = True
        break
    elif list1[6] == list1[4] == list1[2] == "O":
        print(p1+" is the winner")
        flag = True
        break
    elif list1[6] == list1[4] == list1[2] == "X":
        print(p2+" is the winner")
        flag = True
        break
    elif list1[0] == list1[3] == list1[6] == "O":
        print(p1+" is the winner")
        flag = True
        break
    elif list1[0] == list1[3] == list1[6] == "X":
        print(p2+" is the winner")
        flag = True
        break
    elif list1[1] == list1[4] == list1[7] == "O":
        print(p1+" is the winner")
        flag = True
        break
    elif list1[1] == list1[4] == list1[7] == "X":
        print(p2+" is the winner")
        flag = True
        break
    elif list1[2] == list1[5] == list1[8] == "O":
        print(p1+" is the winner")
        flag = True
        break
    elif list1[2] == list1[5] == list1[8] == "X":
        print(p2+" is the winner")
        flag = True
        break
    turns += 1
if not flag:
    print("it is a tie")
