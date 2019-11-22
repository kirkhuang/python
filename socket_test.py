import socket
 
def checkip(ipaddr,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ipaddr,port))
        return True
    except socket.error as e:
        return False
    finally:
        sock.close()
 
if __name__ == '__main__':
    file = open("ip_list.txt")
    checkinfo = open("check_info.txt",'w+')
    line = file.readline()
    while line:
        if line == "":
            continue
        iplist = line.split(' ')
        ipaddr = iplist[0]
        port = int(iplist[1])
        status = checkip(ipaddr,port)
        if status == True:
            info = '%s %s is OK' % (ipaddr, port)+'\n'
            checkinfo.write(info)
        else:
            info = '%s %s is Fail' % (ipaddr, port)+'\n'
            checkinfo.write(info)
        line = file.readline()
    file.close()