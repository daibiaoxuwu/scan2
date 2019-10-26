with open("all_ipv4.txt","r") as f:
    with open("all_ipv6.txt","w") as g:
        for i in f.readlines():
            g.write("2402:f000:1:403:"+i)
            g.write("2402:f000:1:404:"+i)
            g.write("2402:f000:1:405:"+i)
            g.write("2402:f000:1:406:"+i)
            g.write("2402:f000:1:407:"+i)
            g.write("2402:f000:1:408:"+i)
            g.write("2402:f000:1:414:"+i)
            g.write("2402:f000:1:415:"+i)
            g.write("2402:f000:1:416:"+i)
            g.write("2402:f000:1:417:"+i)
        
