# -*- coding: utf-8 -*-
__author__ = 'Yun Zhu'

import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
next_year = today + datetime.timedelta(days=365)

print yesterday, tomorrow, next_year