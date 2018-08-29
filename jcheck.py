''' jcheck '''

import os
import subprocess
import sys

try:
    lis_dir = os.listdir("./testcases")
    tmp = lis_dir.copy()
    for t in lis_dir:
        if 'input' not in t and 'output' not in t and 'problem' not in t:
            tmp.remove(t)
    lis_dir = tmp
except Exception as e:
    print(e)
else:
    n=len(lis_dir)
    n -= 1
    n2 = n//2
    sum = 0
    for i in range(n2):
        f = open('./testcases/'+lis_dir[i],'rb')
        inp_ = f.read()
        f.close()

        os.system('javac {}.java'.format(sys.argv[1]))
        p=subprocess.run(['java',sys.argv[1]],shell=True,check=True,input=inp_,stdout=subprocess.PIPE)
        f = open('./testcases/'+lis_dir[i+n2],'rb')
        outp_ = f.read()
        f.close()
        

        if p.stdout.replace(b'\r',b'').replace(b'\n',b'') == outp_.replace(b'\r',b'').replace(b'\n',b''):
            sum += 1
            print("problem",i)
            print("expected output: ",outp_.replace(b'\r',b'').replace(b'\n',b'').decode())
            print("actual output: ",p.stdout.replace(b'\r',b'').replace(b'\n',b'').decode())
            print("------------------------------------------------")
        else:
            print("failed for problem",i)
            print("input: ",inp_.decode())
            print("expected output: ",outp_.replace(b'\r',b'').replace(b'\n',b'').decode())
            print("actual output: ",p.stdout.replace(b'\r',b'').replace(b'\n',b'').decode())
            print("------------------------------------------------")

    
    print("Test score ",str(sum)+"/"+str(i+1))


#exp....
try:
    p=subprocess.run(['java','-jar','C:\\Users\\Mohath\\Documents\\jtools\\checkstyle.jar','-c','/sun_checks.xml',sys.argv[1] + '.java'],shell=True,check=True,stdout=subprocess.PIPE)
except Exception as e:
    print(e.output.replace(b'\r',b'').decode())
else:
    print(p.stdout.replace(b'\r\n',b'').decode())



