def sort(m,n,d):
    jug1=0
    jug2=0
    step=[[0,0]]
    if d==0:
        print(step)
    elif d==m+n:
        step+=[[m,0],[m,n]]
        for i in step:
            print(i)
    elif m+n<d:
        print("{}L cannot be measured with {]L and {}L jugs".format(d.m,n))
    else:
        while jug1!=d and jug2!=d and(jug1+jug2)!=d :
            if(jug1==0):
                jug1=m
                step.append([jug1,jug2])
            t=min(jug1,n-jug2)
            jug2 += t
            jug1 -= t
            step.append([jug1,jug2])
            if(jug2==n):
                jug2=0
                step.append([jug1,jug2])
            if(jug1==0):
                jug1=m
                step.append([jug1,jug2])
        for i in step:
            print(i)
sort(5,3,4)

   
