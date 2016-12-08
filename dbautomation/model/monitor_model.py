#!/usr/bin/env python
#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.db import connection
import commands
import os

class Monitor(object):
    def __init__(self, userid,nServerid,nMonitortype,nMonitorname,nMonitorvalue,nIsmonitor,nMonitorshell,nDbid,nMonitorid):
        self.userid = str(userid)
        self.nServerid = nServerid
        self.nMonitortype = nMonitortype
        self.nMonitorname = nMonitorname
        self.nMonitorvalue = nMonitorvalue
        self.nMonitorshell = nMonitorshell
        self.nDbid = nDbid
        self.nMonitorid = nMonitorid
        self.nIsmonitor = nIsmonitor

    @classmethod
    def mysqlmonitor(self,userid):
        nsql = 'select user_id as userid,user_role as userrole,is_forbid as isforbid from user_info where user_id=%s'
        cursor = connection.cursor()
        cursor.execute( nsql, [userid])
        row = cursor.fetchone()
        cursor.close()
        return row

    @classmethod
    def getbeforaddportmonitor(self):
        nsql = 'select server_id,server_name from server_data_info'
        cursor = connection.cursor()
        cursor.execute( nsql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    @classmethod
    def portmonitorlist(self):
        nsql = 'select monitor_id,monitor_target_name,monitor_target_value,is_monitor from  server_monitor_prototype a where monitor_type=4'
        cursor = connection.cursor( )
        cursor.execute( nsql)
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def addportmonitor(self,userid,nServerid,nMonitortype,nMonitorname,nMonitorvalue,nIsmonitor):
        nsql = 'select user_role from user_info where user_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [userid])
        row = cursor.fetchone( )
        rowdata = row[0]
        if rowdata == 1:
            nSqlone = 'insert into server_monitor_prototype (monitor_type,monitor_target_name,monitor_target_value,is_monitor) values (%s,%s,%s,%s)'
            cursor = connection.cursor( )
            cursor.execute( nSqlone, [nMonitortype,nMonitorname,nMonitorvalue,nIsmonitor] )
            cursor.close( )
            connection.commit( )
            connection.close( )

    @classmethod
    def getbeforupdateservermonitor(self,nMonitorid):
        nsql = 'select monitor_id,monitor_type,monitor_target_name,monitor_target_value,monitor_shell,is_monitor from  server_monitor_prototype  where monitor_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql,nMonitorid)
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def updateportmonitor(self, nMonitorid,nMonitortype,nMonitorname,nMonitorvalue,nIsmonitor):
        nSqlone = 'update server_monitor_prototype set monitor_type=%s,monitor_target_name=%s,monitor_target_value=%s,is_monitor=%s where monitor_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSqlone, [nMonitortype,nMonitorname,nMonitorvalue,nIsmonitor,nMonitorid] )
        cursor.close( )
        connection.commit( )
        connection.close( )

    @classmethod
    def deleteportmonitor(self, nMonitorid):
        nSqlone = 'delete from  server_monitor_prototype where monitor_id=%s '
        cursor = connection.cursor( )
        cursor.execute( nSqlone, [nMonitorid] )
        cursor.close( )
        connection.commit( )
        connection.close( )

    @classmethod
    def dbmonitorlist(self):
        nsql = 'select monitor_id,monitor_type,monitor_target_name,monitor_shell,is_monitor from server_monitor_prototype a where monitor_type in (1,2)'
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def getbeforadddbmonitor(self):
        nsql = 'select server_id,db_id,db_name from db_data_info'
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def adddbmonitor(self, userid, nMonitortype, nMonitorname, nMonitorshell, nIsmonitor):
        nSqlone = 'insert into server_monitor_prototype (monitor_type,monitor_target_name,monitor_shell,is_monitor) values (%s,%s,%s,%s)'
        cursor = connection.cursor( )
        cursor.execute( nSqlone, [ nMonitortype, nMonitorname, nMonitorshell, nIsmonitor] )
        Monitorid= cursor.lastrowid
        cursor.close( )
        connection.commit( )

        if nMonitortype == 'mysql':
            nbachsql = "insert into server_monitor_relation select Monitorid,server_id,db_id from db_data_info where db_type='mysql' "
            cursor = connection.cursor()
            cursor.execute(nbachsql)
            connection.commit()
        elif nMonitortype == 'redis':
            nbachsql = "insert into server_monitor_relation select Monitorid,server_id,db_id from db_data_info where  db_type='redis'"
            cursor = connection.cursor()
            cursor.execute(nbachsql)
            connection.commit()

    @classmethod
    def getbeforupdatedbmonitor(self, nMonitorid):
        nsql = 'select monitor_id,monitor_type,monitor_target_name,monitor_target_value,monitor_shell,is_monitor from server_monitor_prototype a where monitor_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, nMonitorid )
        rows = cursor.fetchall()
        cursor.close( )
        return rows

    @classmethod
    def updatedbmonitor(self, nMonitorid,nMonitortype,nMonitorname,nMonitorshell,nIsmonitor):
        nSqlone = 'update server_monitor_prototype set monitor_type=%s,monitor_target_name=%s,monitor_shell=%s,is_monitor=%s where monitor_id=%s'
        cursor = connection.cursor()
        cursor.execute( nSqlone,[nMonitortype,nMonitorname, nMonitorshell, nIsmonitor, nMonitorid])
        cursor.close()
        connection.commit()
        connection.close()


    @classmethod
    def osmonitorlist(self):
        nsql = 'select monitor_id,monitor_type,monitor_target_name,monitor_shell,is_monitor from server_monitor_prototype a where monitor_type=3'
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def getbeforaddosmonitor(self):
        nsql = 'select  server_id,server_name from  server_data_info '
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def addosmonitor(self, nMonitortype, nMonitorname, nMonitorshell, nIsmonitor):
        nSqlone = 'insert into server_monitor_prototype (monitor_type,monitor_target_name,monitor_shell,is_monitor) values (%s,%s,%s,%s)'
        cursor = connection.cursor( )
        cursor.execute( nSqlone, [ nMonitortype, nMonitorname, nMonitorshell, nIsmonitor] )
        Monitorid = cursor.lastrowid
        cursor.close( )
        connection.commit( )

        nbachsql = "insert into server_monitor_relation select Monitorid,server_id,0 from server_data_info "
        cursor = connection.cursor( )
        cursor.execute( nbachsql )
        connection.commit( )


    @classmethod
    def updateosmonitor(self, nMonitorid, nMonitortype, nMonitorname, nMonitorshell, nIsmonitor):
        nSqlone = 'update server_monitor_prototype set monitor_type=%s,monitor_target_name=%s,monitor_shell=%s,is_monitor=%s where monitor_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSqlone, [nMonitortype, nMonitorname, nMonitorshell, nIsmonitor, nMonitorid] )
        cursor.close( )
        connection.commit( )
        connection.close( )

    @classmethod
    def osmonitorrelationlist(self):
        nSqlone = 'select a.monitor_id as monitor_id,monitor_target_name,a.server_id as server_id,server_name  from server_monitor_relation a join server_monitor_prototype b on a.monitor_id=b.monitor_id join server_data_info c on a.server_id=c.server_id where monitor_type=3'
        cursor = connection.cursor( )
        cursor.execute( nSqlone )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def getbeforaddosmonitorrelation(self):
        nsql = "select '111111111','ALL' union select monitor_id,monitor_target_name from server_monitor_prototype a where monitor_type=3"
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def addosmonitorrealtion(self, nServerid, nMonitorid):
        if nMonitorid == '111111111':
            nSqlone = 'replace into server_monitor_relation (monitor_id,server_id) select monitor_id,%s from server_monitor_prototype where monitor_type=3'
            cursor = connection.cursor( )
            cursor.execute( nSqlone, [nServerid] )
            cursor.close( )
            connection.commit( )
            connection.close( )
        else:
            nSqlone = 'replace into server_monitor_relation (monitor_id,server_id) select %s,%s '
            cursor = connection.cursor( )
            cursor.execute( nSqlone, [nMonitorid, nServerid] )
            cursor.close( )
            connection.commit( )
            connection.close( )


    @classmethod
    def dbmonitorrelationlist(self):
        nSqlone = 'select a.monitor_id as monitor_id,monitor_target_name,a.db_id as db_id,db_name,a.server_id as server_id,server_name  from server_monitor_relation a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.db_id=c.db_id join server_data_info d on c.server_id=d.server_id where monitor_type=1'
        cursor = connection.cursor( )
        cursor.execute( nSqlone)
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def getbeforadddbmonitorrelation(self):
        nsql = "select '111111111','ALL' union select monitor_id,monitor_target_name from server_monitor_prototype a where monitor_type=1"
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def adddbmonitorrealtion(self, nDbid,nMonitorid):
        if nMonitorid == '111111111' :
            nSqlone = 'replace into server_monitor_relation (monitor_id,server_id,db_id) select monitor_id,(select server_id from db_data_info where db_id=%s),%s from server_monitor_prototype where monitor_type=1'
            cursor = connection.cursor( )
            cursor.execute( nSqlone, [nDbid,nDbid] )
            cursor.close( )
            connection.commit( )
            connection.close( )
        else:
            nSqlone = 'replace into server_monitor_relation (monitor_id,server_id,db_id) select %s,(select server_id from db_data_info where db_id=%s),%s '
            cursor = connection.cursor( )
            cursor.execute( nSqlone, [nMonitorid,nDbid,nDbid] )
            cursor.close( )
            connection.commit( )
            connection.close( )

    @classmethod
    def deletedbmonitorrealtion(self,nDbid,nMonitorid):
        nSqlone = 'delete from server_monitor_relation where monitor_id=%s and db_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSqlone, [nMonitorid,nDbid] )
        cursor.close( )
        connection.commit( )
        connection.close( )

    @classmethod
    def deleteosmonitorrealtion(self, nServerid, nMonitorid):
        nSqlone = 'delete from server_monitor_relation where monitor_id=%s and server_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSqlone, [nMonitorid, nServerid] )
        cursor.close( )
        connection.commit( )
        connection.close( )