def process(ans,g):
    for i in range(403,418):
        if(i>408 and i<414):continue
        out="2402:f000:1:"+str(i)+":"
        for i in range(4):out+=hex(ans[i])[2:]
        out+=":"
        for i in range(4,8):out+=hex(ans[i])[2:]
        out+=":"
        for i in range(8,12):out+=hex(ans[i])[2:]
        out+=":"
        for i in range(12,16):out+=hex(ans[i])[2:]
        out+="\n"
        g.write(out)

import math
with open("111_ipv6.txt","w") as g:
    for i1 in range(64):
        ans=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ans[int(i1/4)]+=int(math.pow(2,i1%4))
        process(ans,g)
        for i2 in range(i1+1,64):
            ans=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ans[int(i1/4)]+=int(math.pow(2,i1%4))
            ans[int(i2/4)]+=int(math.pow(2,i2%4))
            process(ans,g)
            for i3 in range(i2+1,64):
                ans=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ans[int(i1/4)]+=int(math.pow(2,i1%4))
                ans[int(i2/4)]+=int(math.pow(2,i2%4))
                ans[int(i3/4)]+=int(math.pow(2,i3%4))
                process(ans,g)
