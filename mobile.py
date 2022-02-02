print("pls enter the no of items inn store")
n=int(input())
items={}
totalbill=0
bill=[]
not_available=[]
for i in range(n):
    print("pls enter the item name")
    itemname=input()
    print("pls enter the unit price and availability in one line with a space")
    l=list(map(int,input().split(" ")))
    items[itemname]=l
print("pls enter the user required items number")
usernum=int(input())
for i in range(usernum):
    print("pls enter the item name")
    user_item=input()
    if user_item not in items:
        not_available.append(user_item)
    else:
        print("pls enter the units needed")
        user_unit=int(input())
        l1=items[user_item]
        if l1[1]<user_unit:
            not_available.append(user_item)
        else:
            totalbill+=l1[0]*user_unit
            t1=(user_item,user_unit,l1[0]*user_unit)
            bill.append(t1)
print("total cost :")
print(totalbill)
print("bill :")
for i in bill:
     print(i)
print("items not available :")
for i in not_available:
    print(i)