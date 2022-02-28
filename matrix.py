from platformdirs import site_config_dir


l=[]
vowel=['a','e','i','o','u','A','E','I','O','U']
for i in range(int(input())):
    s=""
    string,num=input().split(",")
    for i in range(len(string)):
        if(((i+int(num))%len(string))+1%2==0):
            print(string[(i+int(num))%len(string)])
            if string[((i+int(num))%len(string))] in vowel:
                s+=string[(i+int(num))%len(string)]
    print(s)
