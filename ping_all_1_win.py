import subprocess
for i in range(0,65536):
    try:
        if i%1000==0:print(str(i)+" in 65536")
        ret = subprocess.check_output(["ping", "2402:f000:1:"+hex(i)[2:]+"::1","-w","1","-n","1"])
        print(hex(i)[2:])
    except:pass

