# coding:utf8
import calendar
import time
from datetime import datetime
import pytz


# timestamp ==> datetime
def timestamp2datetime(timestamp):
    return datetime.fromtimestamp(timestamp)


# datetime ==> str
def datetime2str(datetime_obj, str_format="%Y-%m-%d %H:%M:%S"):
    return datetime_obj.strftime(str_format)


# str ==> datetime
def str2datetime(time_str, str_format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(time_str, str_format)


# offset-naive ==> offset-aware
def navie2aware(datetime_obj):
    return datetime_obj.replace(tzinfo=pytz.timezone('UTC'))


# offset-aware ==> offset-naive
def aware2navie(datetime_obj):
    return datetime_obj.replace(tzinfo=None)


def get_wday_and_month_range():
    day_now = time.localtime()
    # day_begin = '%d-%02d-01' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
    # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    w_day, month_range = calendar.monthrange(day_now.tm_year, day_now.tm_mon)
    w_day_now = w_day + day_now.tm_mday - 1
    w_day_now = w_day_now % 7 + 1
    return w_day_now, month_range
    # day_end ='%d-%02d-%02d' % (day_now.tm_year, day_now.tm_mon, month_range)
    # print '月初日期为:',day_begin, '月末日期为:',day_end

if __name__ == "__main__":
    # b = datetime.now()
    # print b
    # a = navie2aware(b)
    # print a
    # print aware2navie(a)
    get_wday_and_month_range()
    pass
