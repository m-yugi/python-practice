num=1994
total=""
while(num>0):
    if num >= 1000:
        total+="M"
        num-=1000
    elif num >= 900:
        total += "CM"
        num-=900
    elif num >= 500:
        total += "D"
        num-=500
    elif num >= 400:
        total += "CD"
        num-=400
    elif num >= 100:
        total += "C"
        num-=100
    elif num >= 90:
        total += "XC"
        num-=90
    elif num >= 50:
        total += "L"
        num-=50
    elif num >= 40:
        total += "XL"
        num-=40
    elif num >= 10:
        total += "X"
        num-=10
    elif num >= 9:
        total += "IX"
        num-=9
    elif num >= 5:
        total += "V"
        num-=5
    elif num >= 4:
        total += "IV"
        num-=4
    elif num >= 1:
        total += "I"
        num-=1   
print(total)