#!/usr/bin/env python
#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.db import connection

class Serverapply(object):
    def __init__(self, nServerip,nServerport,nApplytype,nApplyname,nApplyport,nApplytags,nProjectname):
        self.nServerip = nServerip
        self.nServerport = nServerport
        self.nApplytype = nApplytype
        self.nApplyname = nApplyname
        self.nApplyport = nApplyport
        self.nApplytags = nApplytags
        self.nProjectname = nProjectname

    @classmethod
    def serverapplylist(self):
        nsql='select id,project_name,server_ip,server_port,apply_type,apply_name,apply_port,apply_tags,create_time,update_time from server_apply_info '
        cursor = connection.cursor()
        cursor.execute(nsql)
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def addserverapply(self,nProjectname,nServerip,nServerport,nApplytype,nApplyname,nApplyport,nApplytags):
        nsql = 'insert into server_apply_info (project_name,server_ip,server_port,apply_type,apply_name,apply_port,apply_tags,create_time,update_time) values (%s,%s,%s,%s,%s,%s,%s,now(),now())'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nProjectname,nServerip,nServerport,nApplytype,nApplyname,nApplyport,nApplytags])
        cursor.close( )
        connection.commit( )
        connection.close( )

    @classmethod
    def getprojectname(self):
        nsql = 'select project_name from server_apply_info group by project_name'
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def getapplytype(self,nProjectname):
        nsql = 'select project_name,apply_type from server_apply_info where project_name=%s group by apply_type'
        cursor = connection.cursor( )
        cursor.execute( nsql,[nProjectname] )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def getapplyname(self,nProjectname,nApplytype):
        nsql = 'select project_name,apply_type,server_ip,server_port,apply_name,apply_port,apply_tags from server_apply_info where project_name=%s and apply_type=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql,[nProjectname,nApplytype])
        rows = cursor.fetchall( )
        cursor.close( )
        return rows