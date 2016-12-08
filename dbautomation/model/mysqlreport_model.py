#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.db import connection

class Mysqlreport(object):
    def __init__(self, nDbid, nCreateTime,ndays):
        self.nDbid = nDbid
        self.nCreateTime = nCreateTime
        self.ndays = ndays

    @classmethod
    def Dbdatainfo(self):
        nsql="select a.db_id as db_id,db_name,db_port,db_user,db_allpri_pwd,defaults_db_name,server_name,outer_net,inner_net,use_outer_inner,db_role from db_data_info a join (select db_id from user_db_relation group by db_id) b on a.db_id=b.db_id join server_data_info c on a.server_id=c.server_id where db_type='mysql' order by db_id"
        cursor = connection.cursor()
        cursor.execute(nsql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    @classmethod
    def Dbdatainfobyid(self,nDbid):
        nsql = "select a.db_id as db_id,db_name,db_port,db_user,db_allpri_pwd,defaults_db_name,server_name,outer_net,inner_net,use_outer_inner,db_role from db_data_info a join (select db_id from user_db_relation group by db_id) b on a.db_id=b.db_id join server_data_info c on a.server_id=c.server_id where db_type='mysql' and a.db_id=%s" % (nDbid)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdata1(self,nDbid,nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            print(11111111111)
            nsql = "select db_id,version_values,mysql_status,1day_sql_slow as sql_slow,create_time from server_report_monitor_result where db_id=%s and create_time='%s'" %(nDbid,nCreateTime)
        elif ndays == 7:
            print(22222222222)
            nsql = "select db_id,version_values,mysql_status,7day_sql_slow as sql_slow,create_time from server_report_monitor_result where db_id=%s and create_time='%s'" % (nDbid, nCreateTime)
        elif ndays == 30:
            print(333333333333)
            nsql = "select db_id,version_values,mysql_status,30day_sql_slow as sql_slow,create_time from server_report_monitor_result where db_id=%s and create_time='%s'" % (nDbid, nCreateTime)

        cursor = connection.cursor()
        cursor.execute(nsql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    @classmethod
    def Dbreportdaydata2(self, nDbid, nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select a.db_id,a.monitor_id,round(a.monitor_values,2),abs(round((a.monitor_values-b.monitor_values)/a.monitor_values/120*100,2)) from (select a.db_id as db_id,b.monitor_id as monitor_id,avg(monitor_values) as monitor_values from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_alldbspace' and date(a.create_time)='%s') a join (select a.db_id as db_id,b.monitor_id as monitor_id,avg(monitor_values) as monitor_values from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_alldbspace' and adddate(date(a.create_time),%s)='%s') b on a.db_id=b.db_id" % (nDbid,nCreateTime,nDbid,ndays,nCreateTime)
        elif ndays == 7:
            nsql = "select a.db_id,a.monitor_id,round(a.monitor_values,2),abs(round((a.monitor_values-b.monitor_values)/a.monitor_values/120*100,2)) from (select a.db_id as db_id,b.monitor_id as monitor_id,avg(monitor_values) as monitor_values from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_alldbspace' and date(a.create_time)='%s') a join (select a.db_id as db_id,b.monitor_id as monitor_id,avg(monitor_values) as monitor_values from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_alldbspace' and adddate(date(a.create_time),%s)='%s') b on a.db_id=b.db_id" % (nDbid, nCreateTime, nDbid, ndays, nCreateTime)
        elif ndays == 30:
            nsql = "select a.db_id,a.monitor_id,round(a.monitor_values,2),abs(round((a.monitor_values-b.monitor_values)/a.monitor_values/120*100,2)) from (select a.db_id as db_id,b.monitor_id as monitor_id,avg(monitor_values) as monitor_values from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_alldbspace' and date(a.create_time)='%s') a join (select a.db_id as db_id,b.monitor_id as monitor_id,avg(monitor_values) as monitor_values from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_alldbspace' and adddate(date(a.create_time),%s)='%s') b on a.db_id=b.db_id" % (nDbid, nCreateTime, nDbid, ndays, nCreateTime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdaydata3(self, nDbid, nCreateTime, ndays):
        ndays=int(ndays)
        nsql = "select a.db_id,a.monitor_id,round(a.monitor_values,2),abs(round((a.monitor_values-b.monitor_values)/a.monitor_values/120*100,2)) from (select a.db_id as db_id,b.monitor_id as monitor_id,avg(monitor_values) as monitor_values from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_maxtable' and date(a.create_time)='%s') a join (select a.db_id as db_id,b.monitor_id as monitor_id,avg(monitor_values) as monitor_values from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_maxtable' and adddate(date(a.create_time),%s)='%s') b on a.db_id=b.db_id" % (nDbid, nCreateTime, nDbid, ndays, nCreateTime)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdayqps(self,nDbid,nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select db_id,a.monitor_id as monitor_id,round(real_values/120) as monitor_values,a.create_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_QPS' and a.create_time>=adddate('%s',-%s)" % (nDbid,nCreateTime,ndays)
        elif ndays == 7:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(real_values)/120) as monitor_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_QPS' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid,nCreateTime,ndays)
        elif ndays == 30:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(real_values)/120) as monitor_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_QPS' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid,nCreateTime,ndays)
        print(nsql)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdaytps(self, nDbid, nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select db_id,a.monitor_id as monitor_id,round(real_values/120) as monitor_values,a.create_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_tps' and a.create_time>=adddate('%s',-%s) " % (nDbid, nCreateTime,ndays)
        elif ndays == 7:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(real_values)/120) as monitor_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_tps' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime,ndays)
        elif ndays == 30:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(real_values)/120) as monitor_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_tps' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime,ndays)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdayprocessnum(self, nDbid, nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select db_id,a.monitor_id as monitor_id,round(monitor_values) as avg_values,round(monitor_values) as max_values,round(monitor_values) as max_values,a.create_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_processlistnum' and a.create_time>=adddate('%s',-%s)" % (nDbid, nCreateTime,ndays)
        elif ndays == 7:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(monitor_values)) as avg_values,round(max(monitor_values)) as max_values,round(min(monitor_values)) as max_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_processlistnum' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime, ndays)
        elif ndays == 30:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(monitor_values)) as avg_values,round(max(monitor_values)) as max_values,round(min(monitor_values)) as max_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_processlistnum' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime, ndays)

        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdayreadbuffer(self, nDbid, nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select db_id,a.monitor_id as monitor_id,round(monitor_values*100,2) as avg_values,a.create_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_keybufferreadhits' and a.create_time>=adddate('%s',-%s)" % (nDbid, nCreateTime,ndays)
        elif ndays == 7:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(monitor_values)*100,2) as avg_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_keybufferreadhits' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime,ndays)
        elif ndays == 30:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(monitor_values)*100,2) as avg_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_keybufferreadhits' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime, ndays)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdaywritebuffer(self, nDbid, nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select db_id,a.monitor_id as monitor_id,round(monitor_values*100,2) as avg_values,a.create_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_keybufferwritehits' and a.create_time>=adddate('%s',-%s)" % (nDbid, nCreateTime,ndays)
        elif ndays == 7:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(monitor_values)*100,2) as avg_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_keybufferwritehits' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime,ndays)
        elif ndays == 30:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(monitor_values)*100,2) as avg_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_keybufferwritehits' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime, ndays)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdayinnodbbuffer(self,nDbid, nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select db_id,a.monitor_id as monitor_id,round(monitor_values*100,2) as avg_values,a.create_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_innodbbufferreadhits' and a.create_time>=adddate('%s',-%s)" % (nDbid, nCreateTime,ndays)
        elif ndays == 7:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(monitor_values)*100,2) as avg_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_innodbbufferreadhits' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime,ndays)
        elif ndays == 30:
            nsql = "select db_id,a.monitor_id as monitor_id,round(avg(monitor_values)*100,2) as avg_values,date(a.create_time) from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id where db_id=%s and monitor_target_name ='mysql_num_innodbbufferreadhits' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)" % (nDbid, nCreateTime,ndays)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def Dbreportdayosload(self,nDbid, nCreateTime,ndays):
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select a.avg_values,b.avg_values,c.avg_values,a.day_time from (select c.db_id as db_id,a.monitor_id as monitor_id,round(monitor_values,2) as avg_values,a.create_time as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id where c.db_id=%s and monitor_target_name ='os_num_1mload' and a.create_time>=adddate('%s',-%s)) a join (select c.db_id as db_id,a.monitor_id as monitor_id,round(monitor_values*100,2) as avg_values,a.create_time as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_1mload' and a.create_time>=adddate('%s',-%s)) b on a.db_id=b.db_id and a.day_time=b.day_time join (select c.db_id as db_id,a.monitor_id as monitor_id,round(monitor_values*100,2) as avg_values,a.create_time as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_15mload' and a.create_time>=adddate('%s',-%s)) c on a.db_id=c.db_id and a.day_time=c.day_time" % (nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays)
        elif ndays == 7:
            nsql = "select a.avg_values,b.avg_values,c.avg_values,a.day_time from (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values),2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id where c.db_id=%s and monitor_target_name ='os_num_1mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) a join (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values)*100,2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_1mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) b on a.db_id=b.db_id and a.day_time=b.day_time join (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values)*100,2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_15mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) c on a.db_id=c.db_id and a.day_time=c.day_time" % (nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays)
        elif ndays == 30:
            nsql = "select a.avg_values,b.avg_values,c.avg_values,a.day_time from (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values),2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id where c.db_id=%s and monitor_target_name ='os_num_1mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) a join (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values)*100,2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_1mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) b on a.db_id=b.db_id and a.day_time=b.day_time join (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values)*100,2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_15mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) c on a.db_id=c.db_id and a.day_time=c.day_time" % (nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows
        ndays=int(ndays)
        if ndays == 1:
            nsql = "select a.avg_values,b.avg_values,c.avg_values,a.day_time from (select c.db_id as db_id,a.monitor_id as monitor_id,round(monitor_values,2) as avg_values,a.create_time as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id where c.db_id=%s and monitor_target_name ='os_num_1mload' and a.create_time>=adddate('%s',-%s)) a join (select c.db_id as db_id,a.monitor_id as monitor_id,round(monitor_values*100,2) as avg_values,a.create_time as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_1mload' and a.create_time>=adddate('%s',-%s)) b on a.db_id=b.db_id join (select c.db_id as db_id,a.monitor_id as monitor_id,round(monitor_values*100,2) as avg_values,a.create_time as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_15mload' and a.create_time>=adddate('%s',-%s)) c on a.db_id=c.db_id and a.day_time=c.day_time" % (nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays)
        elif ndays == 7:
            nsql = "select a.avg_values,b.avg_values,c.avg_values,a.day_time from (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values),2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id where c.db_id=%s and monitor_target_name ='os_num_1mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) a join (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values)*100,2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_1mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) b on a.db_id=b.db_id join (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values)*100,2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_15mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) c on a.db_id=c.db_id and a.day_time=c.day_time" % (nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays)
        elif ndays == 30:
            nsql = "select a.avg_values,b.avg_values,c.avg_values,a.day_time from (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values),2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id where c.db_id=%s and monitor_target_name ='os_num_1mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) a join (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values)*100,2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_1mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) b on a.db_id=b.db_id join (select c.db_id as db_id,a.monitor_id as monitor_id,round(max(monitor_values)*100,2) as avg_values,date(a.create_time) as day_time from server_monitor_result a join server_monitor_prototype b on a.monitor_id=b.monitor_id join db_data_info c on a.server_id=c.server_id  where c.db_id=%s and monitor_target_name ='os_num_15mload' and date(a.create_time)>=adddate(date('%s'),-%s) group by date(a.create_time)) c on a.db_id=c.db_id and a.day_time=c.day_time" % (nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays,nDbid, nCreateTime,ndays)
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows