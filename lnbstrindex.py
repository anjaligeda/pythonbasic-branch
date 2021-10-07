q=[]
n=int(input('enter length'))
for i in range(n):
    a=input('enter number = ')
    q.append(a)
    print(q)
print(len(q))
if len(q)>7:
    print(q[1::2])
else:
    print(q[0::2])



