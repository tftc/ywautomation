#!/usr/bin/env python
#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.db import connection

class Login(object):
    def __init__(self, username, npwd):
        self.username = username
        self.npwd = npwd

    @classmethod
    def checklogindata(self,username,npwd):

        nsql='select count(*) as num from user_info where login_name=%s and login_pwd=md5(%s)'
        cursor = connection.cursor()
        cursor.execute(nsql,[username, npwd])
        row = cursor.fetchone( )
        cursor.close( )
        for AccountNum in row:
            return AccountNum

    @classmethod
    def usersessiondata(self, username, npwd):

        nsql = 'select user_id as userid,user_role as userrole,is_forbid as isforbid from user_info where login_name=%s and login_pwd=md5(%s)'
        cursor = connection.cursor( )
        cursor.execute( nsql, [username, npwd])
        row = cursor.fetchone( )
        cursor.close( )
        return row
