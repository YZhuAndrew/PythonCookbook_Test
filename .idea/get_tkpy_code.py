# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'PythonCookbook_Test'

import urllib2

u = urllib2.urlopen('http://www.greenteapress.com/thinkpython/code/')
print u.read()
u.close()