import socket

#Getting from user the urls or the IPs and putting the IP addresses into a list
iplist=[]
more="yes"
while(more=="yes"):
    answer=input("Do you want to give url or IP in IPv4 format? (url/ip)\n")
    if (answer=="url"):
        url=input("Please provide the url.\n")
        ip=socket.gethostbyname(url)
    elif (answer=="ip"):
        ip=input("Please provide the IP address in IPv4 format.\n")
    else:
        print("Please answer with url or ip only!")
        continue
    iplist.append(ip)
    more=input("Do you want to continue? (yes/no)\n")
    

f=open("results.txt", "a")
socket.setdefaulttimeout(60)
for x in iplist:
    #Getting from user the port range for each IP
    print("Please provide the port range that you want to check for the %s IP address." %x)
    first=input("Please provide the first port that you want to check.\n")
    last=input("Please provide the last port that you want to check.\n")
    print("Running port scan for %s IP." %x)
    #Port scan for each IP
    for port in range(int(first),int(last)+1):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Let's check if port %d is open!" %port)
        result=s.connect_ex((x, port))
        #If connect_ex is succesful, the IP, the port that is open and the banner are all written in a file
        if(result==0):
            print("Found port %d open!" %port)
            banner= s.recv(1024)
            print(banner)
            f.write("%s  %d  %s\n" %(x,port,banner))
        else:
            print("Port %d was not open.\n" %port)
        s.close()
        
f.close()