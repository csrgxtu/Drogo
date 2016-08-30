#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# File: main.py
# Desc: QQ 命令行版本
# Date: 20/Aug/2016
from qqbot import QQBot
from UI import *
import pickle

def GetNickName(Contacts, number):
    for contact in Contacts:
        if contact[0] == number:
            return contact[1]

    return None

def GetNumber(Contacts, nickname):
    for contact in Contacts:
        if contact[1].encode == nickname:
            return contact[0]

    return None

if __name__=='__main__':
    # start and login qq first
    bot = QQBot()
    bot.Login()
    Buddies = bot.buddy
    Groupes = bot.group
    Discusses = bot.discuss
    Contacts = []
    for buddy in Buddies:
        Contacts.append(buddy)
    for group in Groupes:
        Contacts.append(group)
    for discuss in Discusses:
        Contacts.append(discuss)

    class TestCmd(Command):
        def do_echo(self, *args):
            '''echo - Just echos all arguments'''
            return ' '.join(args)
        def do_raise(self, *args):
            raise Exception('Some Error')

        def do_contact(self, *args):
            if args[0] == 'buddy':
                return bot.buddyStr.replace('?', '')
            elif args[0] == 'group':
                return bot.groupStr.replace('?', '')
            elif args[0] == 'discuss':
                return bot.discussStr.replace('?', '')

        def do_alias(self, *args):
            # first, load the previous alias
            try:
                alias = pickle.load(open('alias.pkl', 'rb'))
            except:
                alias = []

            # insert the current alias into the previous
            qqId = args[0]
            nickname = args[1]

            existFlag = False
            for alia in alias:
                if alia[0] == qqId:
                    existFlag = True
                    alia[1] = nickname
                    break

            if not existFlag:
                alias.append([qqId, nickname])

            output = open('alias.pkl', 'wb')
            pickle.dump(alias, output)
            output.close()

            return 'Set alias: ' + nickname + '(' + qqId + ')'

        def do_listalias(self, *args):
            try:
                alias = pickle.load(open('alias.pkl', 'rb'))
            except:
                alias = []

            outputStr = ''
            for alia in alias:
                outputStr += alia[1] + ' : ' + alia[0] + '\n'

            return outputStr

        def do_number(self, *args):
            nickname = args[0]
            number = GetNumber(Contacts, args[0].encode('utf-8'))
            return number

        def do_sendmsg(self, *args):
            msgType = args[0]
            number = int(args[1])
            nickname = GetNickName(Contacts, number)

            bot.send(msgType, number, ' '.join(args[2:]))
            return '->' + nickname.decode('utf-8') + '(' + str(number) + '): ' + ' '.join(args[2:])

    c=Commander('Drogo', cmd_cb=TestCmd())

    #Test asynch output -  e.g. comming from different thread
    import time
    def run():
        while True:
            time.sleep(3)
            msg = bot.poll()
            if msg[0] == '':
                continue

            nickname = GetNickName(Contacts, msg[1])
            c.output(nickname + '(' + str(msg[1]) + '): ' + msg[3], 'green')

    t=Thread(target=run)
    t.daemon=True
    t.start()

    #start main loop
    c.loop()
