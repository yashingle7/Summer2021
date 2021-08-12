#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

f = cgi.FieldStorage()
cmd = f.getvalue("x")
val = cmd.split()

#Creating deployment
if  val[0]=="1":
    dname = val[2]
    iname = val[1]
    o=sp.getoutput("sudo  kubectl create deployment {} --image={} ".format(dname,iname))
    print(o)

#Creating pod
elif  val[0]=="2":
    pname = val[2]
    iname = val[1]
    o=sp.getoutput("sudo  kubectl run {} --image={} ".format(pname,iname))
    print(o)

#Delete pod
elif  val[0]=="3":
    pname = val[1]
    o=sp.getoutput("sudo  kubectl delete pod {}  ".format(pname))
    print(o)

#delete deployment
elif  val[0]=="4":
    dname = val[1]
    o=sp.getoutput("sudo  kubectl delete deployment {} ".format(dname))
    print(o)

#expose deployment
elif  val[0]=="5":
    dname = val[1]
    port_no = val[2]
    etype  = val[3]
    o=sp.getoutput("sudo  kubectl expose deployment {} --type={} --port={} ".format(dname,etype,port_no))
    print(o)

#scale deployment
elif  val[0]=="6":
    dname = val[1]
    replica= val[2]
    o=sp.getoutput("sudo  kubectl scale deployment {} --replicas={} ".format(dname,replica))
    print(o)

#list pods
elif val[0]=="7":
    o=sp.getoutput("sudo  kubectl get pods")
    print(o)

#list deployments
elif val[0]=="8":
    o=sp.getoutput("sudo  kubectl get deployments ")
    print(o)

#list services
elif val[0]=="9":
    o=sp.getoutput("sudo  kubectl get svc ")
    print(o)

#thank you note
elif val[0]=="10":

    print("WELCOME")

#error
else:
    val[0]=="404"
    print("Something went wrong.....")
