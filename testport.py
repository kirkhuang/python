#!/usr/bin/env python
# coding:utf-8

import socket



# 测试git


NORMAL = 0
ERROR = 1
TIMEOUT = 5


def ping(ip, port, timeout=TIMEOUT):
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (str(ip), int(port))
        status = cs.connect_ex((address))
        cs.settimeout(timeout)
        # this status is returnback from tcpserver
        if status != NORMAL:
            print(str(port) + " ERROR")
        else:
            print(str(port) + " NORMAL")
    except Exception as e:
        print("ERROR")
        print("error:%s" % e)
        return ERROR
    return NORMAL


# if __name__ == '__main__':
#     if len(sys.argv) < 3:
#         print('请按照如下格式使用: ./tcp.py www.jb51.net 80')
#         sys.exit(1)
#     ip = sys.argv[1]
#     port = sys.argv[2]
#     try:
#         timeout = sys.argv[3]
#     except IndexError as e:
#         timeout = TIMEOUT
#     ping(ip, port, timeout)

for i in range(64438):
    ping('192.168.31.54', i, 5)
