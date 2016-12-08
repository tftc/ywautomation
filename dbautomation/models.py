#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.db import connection

class Userinfo(models.Model):
    def my_custom_sql(selft):
        nUsername = selft['username']
        nPassword = selft['password']
        cursor = connection.cursor(selft)
        cursor.execute( "select count(*) into nNum from user_info where login_name=%s and  and login_pwd=%s", [nUsername,nPassword])
        row = cursor.fetchone( )
        return row

