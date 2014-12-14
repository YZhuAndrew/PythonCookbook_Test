# -*- coding: utf-8 -*-
__author__ = 'Yun'

'''
import time
import os
import sys
import sched

schedule = sched.scheduler(time.time, time.sleep)


def perform_command(cmd, inc):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    os.system(cmd)


def main(cmd, inc=60):
    schedule.enter(0, 0, perform_command, (cmd, inc))
    schedule.run()

if __name__ == '__main__':
    numargs = len(sys.argv) - 1
    if numargs < 1 or numargs > 2:
        print "usage: " + sys.argv[0] + " command [seconds_delay]"
        sys.exit(1)
    cmd = sys.argv[1]
    if numargs < 3:
        main(cmd)
    else:
        inc = int(sys.argv[2])
        main(cmd, inc)
'''

'''
import sched
import time

s = sched.scheduler(time.time, time.sleep)


def print_time():
    print "From print_time", time.time()


def print_some_times():
    print time.time()
    s.enter(5, 1, print_time, ())
    s.enter(10, 1, print_time, ())
    s.run()
    print time.time()

print_some_times()
'''

'''
def re_run(num):
    print num
    num += 1
    if num > 50:
        print 'end'
    else:
        re_run(num)

re_run(2)
'''

import sys
import os
import time
import sched

s = sched.scheduler(time.time, time.sleep)


def print_time():
    print time.time()


def print_time_scheduler(steptime):
    s.enter(steptime, 0, print_time, ())
    s.run()
    print_time_scheduler(steptime)


print_time_scheduler(0.5)

perform_command()