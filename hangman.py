import random
life=5
s=["apple","ball","cat"]
e=list(random.choice(s))
u=[]
for i in range(len(e)):
        u.append('-')
while(1):
    if((life==0) or ('-' not in u)):
        break
    print("".join(u))
    user=input("enter ur choice")
    if(user in e):
        ww=e.count(user)
        while(ww>0):
            www=e.index(user)
            u[www]=user
            e[www]=""
            ww-=1
    else:
        life-=1
    print("life",life)
print("".join(u))
if(life==0):
    print("You lost")
else:
    print("You win")
