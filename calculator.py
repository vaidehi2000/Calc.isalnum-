import math

def calculate(i,opn,opr, j ):
    a = opn[i]
    b = opn[i+1]
    if(j=='/'): 
        c = a/b
    elif(j=='*'):
        c=a*b
    elif(j=='+'):
        c=a+b
    elif(j=='-'):
        c=a-b
    opn.remove(a)
    opn.remove(b)
    opn.insert(i,c)
    opr.pop(i)

#----------------------------------------

def choose(opr,opn,r):
    c = opr.count(r)
    while(c!=0):
        j = opr.index(r)
        calculate(j,opn,opr,opr[j])
        c-=1

#=========================================

n = input()
#ns = n.split(" ")
#ns_n = "".join(ns)
#if(ns_n.isalnum()):
#    print("*")
#else:
op = ['+', '-','/','*']
opn = []
opr = []
j=0
for i in range(len(n)):
    if(n[i] in op):
        opr.append(n[i])
        opn.append(float(n[j:i]))
        j=i+1
opn.append(float(n[j:len(n)]))

choose(opr,opn,'/')
choose(opr,opn,'*')
choose(opr,opn,'+')
choose(opr,opn,'-')

k = int(opn[0])
c = math.ceil(opn[0])
if(k==c):
    print(k)
else:
    print("{} ~ {:.2f}".format(opn[0],opn[0]))
