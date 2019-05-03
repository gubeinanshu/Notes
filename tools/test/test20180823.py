# -*- coding: UTF-8 -*-

import time
import os


# 获取文件的大小,结果保留两位小数，默认单位单位为 KB
def get_file_size(file_path, unit=1, reserved=2):
    """获取文件的大小,结果保留两位小数，默认单位单位为 KB"""
    file_path = unicode(file_path, 'utf8')
    fsize = os.path.getsize(file_path)
    fsize = fsize/float(1024**unit)
    return round(fsize, reserved)


# 把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12
def timestamp2time(timestamp):
    """把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12"""
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)


# 获取文件的访问时间
def get_file_access_time(file_path):
    """获取文件的访问时间"""
    file_path = unicode(file_path, 'utf8')
    t = os.path.getatime(file_path)  # 得到时间戳
    return timestamp2time(t)


# 获取文件的创建时间v
def get_file_create_time(file_path):
    """获取文件的创建时间"""
    file_path = unicode(file_path, 'utf8')
    t = os.path.getctime(file_path)
    return timestamp2time(t)


# 获取文件的修改时间
def get_file_modify_time(file_path):
    """获取文件的修改时间"""
    file_path = unicode(file_path, 'utf8')
    t = os.path.getmtime(file_path)
    return timestamp2time(t)


if __name__ == "__main__":
    # print get_file_size("./test20180822.py")
    print get_file_access_time("./test20180821.py")
    print get_file_create_time("./test20180821.py")
    print get_file_modify_time("./test20180821.py")
