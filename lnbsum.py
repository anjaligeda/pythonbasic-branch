#
q=[]
for i in range(5):
    a=int(input('enter number = '))
    if a<=9:
        continue
    else:
        q.append(a)
print(sum(q))        