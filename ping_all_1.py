import subprocess
for i in range(0,65536):
    try:
        ret = subprocess.check_output(["ping6", "2402:f000:1:"+hex(i)[2:]+"::1","-w","1"])
        print(hex(i)[2:])
    except:pass
