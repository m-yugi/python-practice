def isVowel(c):
    return (c=="A" or c=="E" or c=="I" or c=="O" or c=="U" or c=="a" or c=="e" or c=="i" or c=="o" or c=="u")
str="projections"
index=-1
for i in range(len(str)):
    if(isVowel(str[i])):
        index=i
        break
s=str[index:]+str[0:index]+"Ny"
print(s)