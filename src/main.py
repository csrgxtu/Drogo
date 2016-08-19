#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: main.py
# Desc: 微信聊天
# Date: 19/Aug/2016
# from weixin import WebWeixin
from UI import *

if __name__=='__main__':
    class TestCmd(Command):
        def do_echo(self, *args):
            '''echo - Just echos all arguments'''
            return ' '.join(args)
        def do_raise(self, *args):
            raise Exception('Some Error')
        def do_sendMsg(self, *args):
            return ''.join(args)

    c=Commander('Drogo', cmd_cb=TestCmd())

    #Test asynch output -  e.g. comming from different thread
    import time
    def run():
        while True:
            time.sleep(3)
            c.output('I am Khal Drogo:ME', 'green', 'right')
    t=Thread(target=run)
    t.daemon=True
    t.start()

    #start main loop
    c.loop()
