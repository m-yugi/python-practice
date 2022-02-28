q1=[]
q2=[]
q3=[]
q4=[]
limit=10
q1count=0
q2count=0
q3count=0
q4count=0
while(True):
    pat=int(input())
    if(pat<2):
        q1count+=1
        q1.append(q1count)
    elif(pat>60):
        q2count+=1
        q2.append(q2count)
    elif(q1count==limit and q2count==limit):
        q4count+=1
        q4.append(q4count)
    else:
        q3count+=1
        q3.append(q3count)
    if(pat<0):
        break
def print_stat():
    print("q1 status: ",q1count)
    print("q2 status: ",q2count)
    print("q3 status: ",q3count)
    print("q4 status: ",q4count)
print_stat()
