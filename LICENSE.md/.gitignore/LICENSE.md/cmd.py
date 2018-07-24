import subprocess
from time import sleep

print("cmd start")
child = child.py
p = subprocess.Popen(child,bufsize =1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout_data,stderr_data = p.communicate()

print(stdout_data.decode('cp932').rstrip())

print("cmd end")
