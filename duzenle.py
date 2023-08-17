def make_better(a):
    a=a.split()
    b=""
    flag=False
    sayac=0
    for i in a:
        if(i=="Drawer"):
            flag=True
            
        if(flag):
            
                b+=i+" "

    text=""
    for x in b :
        if (x==')'):
            text+=x+'\n'
        elif (b[sayac-4]=='L' and b[sayac]=='l' ):

            #trying to do above
            
            text+=x+'\n'
        elif (x=='%'):
            text+=x+'\n'
        else :
            text+=x
        sayac=sayac+1

    return (text)





