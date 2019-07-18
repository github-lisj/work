#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2019年7月17日

@author: lisj
'''
import datetime


def getCurrentDate():
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return nowTime

