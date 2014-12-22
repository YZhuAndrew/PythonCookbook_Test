# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'PythonCookbook_Test'

class Time(object):
    ''' Represents the time of day. '''

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

start = Time(11, 00, 00)

Time.print_time(start)  # use function syntax
start.print_time()      # use method syntax
print start.__dict__

def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

print_attributes(start)