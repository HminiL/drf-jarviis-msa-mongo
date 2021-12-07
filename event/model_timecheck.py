from datetime import datetime

from icecream import ic


class ScheduleCheck(object):

    def __init__(self):
        pass

    def start(self):
        start_time = '2021-11-30T09:51:25.830000+09:00'
        d_start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%f+09:00')
        time2 = '2021-11-30'
        d_start2 = datetime.strptime(time2, '%Y-%m-%d')
        ic(d_start, d_start2)

if __name__ == '__main__':
    sc = ScheduleCheck()
    sc.start()