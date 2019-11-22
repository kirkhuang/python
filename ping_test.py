import subprocess

def pingCHK(ip):
    num = 10
    wait = 1000
    # 这种方式，终端不会显示运行结果
    ping = subprocess.Popen("ping -n {} -w {} {}".format(num, wait, ip), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exit_code = ping.wait()
    if exit_code != 0:
        return False
    else:
        return True


print(pingCHK('127.0.0.1'))
