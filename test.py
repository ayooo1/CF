import subprocess

res = subprocess.check_output('tasklist /FI "IMAGENAME eq Chrome.exe"')
res = res.decode().split('\n')


hm = {}
for x in res[3:]:
    hm[x.split()[0]] = [x.split()[1:]]+hm.get(x.split()[0],[])
    print(hm[x.split()[0]])
    break
 