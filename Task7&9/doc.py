#!/usr/bin/python3

print("content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

import cgi
import subprocess as sp

f = cgi.FieldStorage()
cmd = f.getvalue("x")
val = cmd.split()

#launch a new container
if  val[0]=="1":

    cname = val[2]
    iname = val[1]
    o=sp.getoutput("sudo docker run -dit --name={} {}".format(cname,iname))
    print(o)

#stop running container
elif  val[0]=="2":

    cname = val[1]
    o=sp.getoutput("sudo  docker stop {} ".format(cname))
    print(o)

#Delete container
elif  val[0]=="3":
    cname = val[1]
    o=sp.getoutput("sudo docker rm -f {}".format(cname))
    print(o)

#Download an image
elif  val[0]=="4":
    dname = val[1]
    o=sp.getoutput("sudo docker pull {}".format(dname))
    print(o)

#Execute a shell
elif  val[0]=="5":

    cname = val[1]
    o=sp.getoutput("sudo docker exec -dit {} ".format(cname))
    print(o)

#list running container
elif  val[0]=="6":

    o=sp.getoutput("sudo docker ps")
    print(o)

#list all the container
elif val[0]=="7":
    o=sp.getoutput("sudo docker ps -a")
    print(o)

#List all images
elif val[0]=="8":
    o=sp.getoutput("sudo docker images")
    print(o)

#Thank you note
elif val[0]=="9":

    print("WELCOME")

#Error
else:
    val[0]=="404"
    print("Something went wrong...")
