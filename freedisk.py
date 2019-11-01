#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ctypes
import os
import platform
import time
import re
# import sys


def get_free_space(folder):
    """ Return folder/drive free space (in bytes)
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder),
                                                   None, None,
                                                   ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 / 1024
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize / 1024 / 1024


# 判断磁盘使用率,小于50 true
def get_value():
    if get_free_space('e:\\') / 399 * 100 < 50:
        return True
    return False


# print(get_free_space('e:\\'), 'GB')


# 判断修改时间，大于7天的true
def file_modify_in(file_path, time_interval='7d'):
    current_time = time.time()
    # os.path.getmtime 返回最后修改时间
    if current_time - os.path.getmtime(
            file_path) < translate_time_interval_to_second(time_interval):
        return False
    return True


def translate_time_interval_to_second(time_interval):
    date_interval = str(time_interval.lower())
    pattern = re.compile(r'\d+')
    match = pattern.match(date_interval)
    date_interval_number = None
    if match:
        date_interval_number = int(match.group())
    else:
        raise IOError("Input {0} can't translate to second."
                      "Current support d(day)/h(hour)/m(min)/s(sec)".format(
                          date_interval))
    if date_interval.endswith('d') or date_interval.endswith('day'):
        return date_interval_number * 24 * 3600
    elif date_interval.endswith('h') or date_interval.endswith('hour'):
        return date_interval_number * 3600
    elif date_interval.endswith('m') or date_interval.endswith('min'):
        return date_interval_number * 60
    elif date_interval.endswith('s') or date_interval.endswith('sec'):
        return date_interval_number
    else:
        raise IOError("Input {0} cant't translate to second."
                      "Current support d(day)/h(hour)/m(min)/s(second)".format(
                          date_interval))


# while get_free_space_mb('e:\\') <= 164 * 50 / 100:
#     pass

# 待处理目录
del_dir = ['E:\\程序A\\车辆原始数据1\\img1\\', 'E:\\程序B\\车辆原始数据1\\img1\\']

# print(os.listdir(del_dir))


# 获取目录下所有文件
def getAllDirDE(path):
    stack = []
    for n in path:
        stack.append(n)

    # 处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        # 从栈里取出数据
        # []
        dirPath = stack.pop()
        # print(dirPath)
        # 目录下所有文件
        filesList = os.listdir(dirPath)
        # print(filesList)
        # 处理每一个文件，如果是普通文件则打印出来，如果是目录则将该目录的地址压栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                # 打印目录名
                print("目录：" + fileName)
                if not os.listdir(fileAbsPath):
                    # 删除空目录
                    os.rmdir(fileAbsPath)
                    print("删除目录：" + fileAbsPath)
                else:
                    # 非空目录入栈
                    stack.append(fileAbsPath)
                # ["B", "E", "F"]
            else:
                # 删除普通文件
                # if file_modify_in(fileAbsPath,
                #                   time_interval='7d') and get_value():
                if file_modify_in(fileAbsPath, time_interval='7d'):
                    # print(file_modify_in(fileAbsPath, time_interval='7d'))
                    # print(get_value())
                    print("普通文件删除：" + fileAbsPath)
                    os.remove(fileAbsPath)
                else:
                    print("普通文件：" + fileAbsPath)


while 1 == 1:
    getAllDirDE(del_dir)
    # 休眠10分钟
    for i in range(10):
        print("已休眠 %d 分钟" % i)
        print("磁盘使用率：%.2f%%" % ((399 - get_free_space('e:\\')) / 399 * 100))
        time.sleep(60)
        i += 1

# print(get_value())
# print("--------")
# print(file_modify_in("E:\\新建\\8、软件研发部\\V2\\111.txt", time_interval='6d'))
