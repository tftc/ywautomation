#!/usr/bin/env python
#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.db import connection

class Dbgraphshow(object):
    def __init__(self, nDbid, nStarttime,nEndtime,nServerid):
        self.nDbid = nDbid
        self.nStarttime = nStarttime
        self.nEndtime = nEndtime
        self.nServerid = nServerid

    @classmethod
    def mysqlqpsdata(self,nDbid,nStarttime,nEndtime):
        nsql="select a.create_time,round(real_values) as qps from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_QPS' and a.create_time>='%s' and a.create_time<='%s'" % (nDbid,nStarttime,nEndtime)
        print nsql
        cursor = connection.cursor()
        cursor.execute(nsql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    @classmethod
    def mysqlidusdata(self, nDbid, nStarttime, nEndtime):
        nsql = "select a.create_time,insertnum,deletenum,updatenum,selectnum from (select a.create_time as create_time,round(real_values) as insertnum from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_Cominsert' and a.create_time>='%s' and a.create_time<='%s' and real_values!='') a join (select a.create_time as create_time,round(real_values) as deletenum from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_Comdelete' and a.create_time>='%s' and a.create_time<='%s' and real_values!='') b on a.create_time=b.create_time join  (select a.create_time as create_time,round(real_values) as updatenum from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_Comupdate' and a.create_time>='%s' and a.create_time<='%s' and real_values!='') c on a.create_time=c.create_time join (select a.create_time as create_time,round(real_values) as selectnum from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_Comselect' and a.create_time>='%s' and a.create_time<='%s' and real_values!='') d on a.create_time=d.create_time" % (nDbid,nStarttime,nEndtime,nDbid,nStarttime,nEndtime,nDbid,nStarttime,nEndtime,nDbid,nStarttime,nEndtime)
        cursor = connection.cursor()
        cursor.execute(nsql)
        rows = cursor.fetchall()
        cursor.close( )
        return rows

    @classmethod
    def mysqlprocesslistnum(self, nDbid, nStarttime, nEndtime):
        nsql = "select a.create_time,round(monitor_values) as qps from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_processlistnum' and a.create_time>='%s' and a.create_time<='%s'" % (nDbid, nStarttime, nEndtime)

        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows


    @classmethod
    def mysqlnumtmptable(self, nDbid, nStarttime, nEndtime):
        nsql = "select a.create_time,round(real_values) as qps from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_tmptable' and a.create_time>='%s' and a.create_time<='%s'" % (nDbid, nStarttime, nEndtime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def mysqlkeybufferreadhits(self, nDbid, nStarttime, nEndtime):
        nsql = "select a.create_time,round(monitor_values,4)*100 as qps from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_keybufferreadhits' and a.create_time>='%s' and a.create_time<='%s'" % (nDbid, nStarttime, nEndtime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def mysqlkeybufferwritehits(self, nDbid, nStarttime, nEndtime):
        nsql = "select a.create_time,round(monitor_values,4)*100 as qps from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_keybufferwritehits' and a.create_time>='%s' and a.create_time<='%s'" % (nDbid, nStarttime, nEndtime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def mysqlinnodbbufferreadhits(self, nDbid, nStarttime, nEndtime):
        nsql = "select a.create_time,round(monitor_values,4)*100 as qps from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.db_id=%s and monitor_target_name='mysql_num_innodbbufferreadhits' and a.create_time>='%s' and a.create_time<='%s'" % (nDbid, nStarttime, nEndtime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def osiouserd(self, nServerid, nStarttime, nEndtime):
        nsql = "select a.create_time,round(monitor_values,2) as qps from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.server_id=%s and monitor_target_name='os_num_iouserd' and a.create_time>='%s' and a.create_time<='%s'" % (nServerid, nStarttime, nEndtime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def osfreecpu(self, nServerid, nStarttime, nEndtime):
        nsql = "select a.create_time,round(monitor_values,4)*100 as qps from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.server_id=%s and monitor_target_name='os_num_cpuunused' and a.create_time>='%s' and a.create_time<='%s'" % (
        nServerid, nStarttime, nEndtime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def osload(self, nServerid, nStarttime, nEndtime):
        nsql = "select a.create_time,1load,5load,15load from (select a.create_time as create_time,round(monitor_values,2) as 1load from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.server_id=%s and monitor_target_name='os_num_1mload' and a.create_time>='%s' and a.create_time<='%s') a join  (select a.create_time as create_time,round(monitor_values,2)  as 5load from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.server_id=%s and monitor_target_name='os_num_5mload' and a.create_time>='%s' and a.create_time<='%s') b on a.create_time=b.create_time join (select a.create_time as create_time,round(monitor_values,2)  as 15load from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where a.server_id=%s and monitor_target_name='os_num_15mload' and a.create_time>='%s' and a.create_time<='%s') c on a.create_time=c.create_time" % (nServerid, nStarttime, nEndtime,nServerid, nStarttime, nEndtime,nServerid, nStarttime, nEndtime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows