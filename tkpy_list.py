# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'PythonCookbook_Test'


def cumulative_sum(number_list):
    new_number_list = []
    for i in range(len(number_list)):
        new_number_list.append(sum(number_list[:(i + 1)]))
    return new_number_list


print cumulative_sum([1, 2, 3, 4, 5])