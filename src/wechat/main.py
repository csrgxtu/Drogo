#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: main.py
# Desc: 微信聊天
# Date: 19/Aug/2016
from weixin import WebWeixin
import logging
from UI import *

if __name__=='__main__':
    logger = logging.getLogger(__name__)
    import coloredlogs
    # coloredlogs.install(level='DEBUG')


    class TestCmd(Command):
        def do_echo(self, *args):
            '''echo - Just echos all arguments'''
            return ' '.join(args)
        def do_raise(self, *args):
            raise Exception('Some Error')

        def do_sendmsg(self, *args):
            webwx.sendMsg(args[0], ' '.join(args[1:]))
            return '->' + args[0] + ': ' + ' '.join(args[1:])

        def do_receivemsg(self, *args):
            return args[0] + ': ' + ' '.join(args[1:])

    c=Commander('Drogo', cmd_cb=TestCmd())

    #Test asynch output -  e.g. comming from different thread
    # import time
    webwx = WebWeixin(c)
    webwx.start()
    def run():
        webwx.listenMsgMode(c)
        # while True:
    #         time.sleep(3)
    #         # c.output('I am Khal Drogo:ME', 'green', 'right')
    t=Thread(target=run)
    t.daemon=True
    t.start()

    #start main loop
    c.loop()
    webwx.quit()
