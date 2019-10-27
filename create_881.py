with open("new_ipv6.txt","w") as g:
    for i in range(256):
        for j in range(256):
            g.write("2402:f000:1:881::"+str(i)+":"+str(j)+"\n")
