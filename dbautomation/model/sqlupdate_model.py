#!/usr/bin/env python
#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.db import connection
import MySQLdb

class SqlUpdate(object):
    def __init__(self, userid,dbid,sqlcontent,userrole,taskid,executetype):
        self.userid =  str(userid)
        self.dbid = str(dbid)
        self.sqlcontent = sqlcontent.encode('utf-8')
        self.userrole = str(userrole)
        self.taskid = str(taskid)
        self.executetype = str(executetype)

    @classmethod
    def mysqlinfolist(self,userid):
        nSql = 'select c.db_id as db_id,server_name,outer_net,inner_net,db_name,db_type,db_port,c.server_id from user_info a join user_db_relation b on a.user_id=b.user_id join db_data_info c on b.db_id=c.db_id join server_data_info d on c.server_id=d.server_id  where a.user_id=%s and is_forbid=1 '
        cursor = connection.cursor( )
        cursor.execute( nSql, [userid] )
        rows = cursor.fetchall()
        cursor.close( )
        return rows

    @classmethod
    def addmysqlsqltask(self, dbid,sqlcontent,nUserid):
        nSql = 'select outer_net,inner_net,use_outer_inner,db_port,db_user,db_allpri_pwd,defaults_db_name from db_data_info a join server_data_info b on a.server_id=b.server_id  where a.db_id=%s'
        cursor = connection.cursor( )
        cursor.execute(nSql, [dbid])
        rows = cursor.fetchone( )
        cursor.close( )

        nOuternet = rows[0]
        nInnernet = rows[1]
        nUseoutinner = rows[2]
        nDbport = rows[3]
        nDBuser = rows[4]
        nDballpripwd = rows[5]
        nDefaultdbname = rows[6]

        print rows
        if nUseoutinner == 1:
            nNet=nOuternet
        elif nUseoutinner == 2:
            nNet=nInnernet

        nUpdateType = 1
        nTaskSql='insert into sql_update_task_info(user_id,db_id,update_type,sql_data) values(%s,%s,%s,%s)'
        cursor = connection.cursor()
        cursor.execute(nTaskSql,[nUserid,dbid,nUpdateType,sqlcontent])
        taskid=cursor.lastrowid
        cursor.close( )
        connection.commit()
        connection.close()

        nIncepsql = '/*--user=%s;--password=%s;--host=%s;--enable-check;--port=%d;*/' %(nDBuser,nDballpripwd,nNet,nDbport) + '\n'  \
              + 'inception_magic_start;' + '\n' \
              + sqlcontent.encode('utf8') + '\n' \
              + 'inception_magic_commit;'

        nIncepsql=nIncepsql.encode('utf-8').decode('latin-1')

        conn=MySQLdb.connect(host="host_name",user="user",passwd="pwd",db="db_name",port=6669)
        cursor = conn.cursor( )
        cursor.execute(nIncepsql)
        result = cursor.fetchall( )
        cursor.close( )
        conn.close( )
        for row in result:
            nCheckid=row[0]
            nCheckstage =row[1]
            nErrlevel=row[2]
            nStagestatus=row[3]
            nErrormessage=row[4].encode('utf8') 
            nChecksql=row[5].encode('utf8') 
            nAffectedrows=row[6]

            checkSql = 'insert into sql_check_task_info(task_id,check_id,check_stage,err_level,stage_status,error_messge,check_sql,affected_row) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor = connection.cursor( )
            cursor.execute(checkSql,[taskid,nCheckid,nCheckstage,nErrlevel,nStagestatus,nErrormessage,nChecksql,nAffectedrows])
            cursor.close()
            connection.commit()
            connection.close()

    @classmethod
    def mysqlunexecutetask(self, userid,userrole):
        if userrole == 1:
            nSql = 'select task_id,user_name,db_name,task_type,update_type,submit_time from sql_update_task_info a left join user_info b on a.user_id=b.user_id left join db_data_info c on a.db_id=c.db_id left join server_data_info d on c.server_id=d.server_id where task_type=0 and task_style=0 order by submit_time desc'
        else:
            nSql = 'select task_id,user_name,db_name,task_type,update_type,submit_time from sql_update_task_info a left join user_info b on a.user_id=b.user_id left join db_data_info c on a.db_id=c.db_id where a.user_id=%s and task_type=0 and task_style=0 order by submit_time desc' % (userid)
        cursor = connection.cursor( )
        cursor.execute( nSql)
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def mysqlsqlcontentinfo(self, taskid):
        nsql='select update_type from sql_update_task_info where task_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [taskid] )
        row = cursor.fetchall( )
        for nNum in row:
            rowdata = nNum[0]
            if rowdata == '1':
                nSqlone = 'select user_name,db_name,sql_data from sql_update_task_info a join user_info b on a.user_id=b.user_id join db_data_info c on a.db_id=c.db_id where a.task_id=%s'
                cursor = connection.cursor()
                cursor.execute(nSqlone, [taskid])
                rows = cursor.fetchall()
                cursor.close()
                return rows
            elif rowdata == '2':
                nSqlone = 'select user_name,db_name,sql_data from sql_update_task_info a join user_info b on a.user_id=b.user_id join db_data_info c on a.db_id=c.db_id where a.task_id=%s'
                cursor = connection.cursor( )
                cursor.execute( nSqlone, [taskid] )
                rows = cursor.fetchall( )
                cursor.close( )
                return rows

    @classmethod
    def selectmysqlsqltask(self, taskid,userid):
        nsql = 'select update_type from sql_update_task_info where task_id=%s'
        cursor = connection.cursor( )
        cursor.execute(nsql,[taskid])
        row = cursor.fetchone( )
        rowdata = row[0]
        if rowdata == '1':
            nSqlone = 'select task_id,update_type,user_name,db_name,sql_data,c.db_id as db_id from sql_update_task_info a join user_info b on a.user_id=b.user_id join db_data_info c on a.db_id=c.db_id where a.task_id=%s order by submit_time desc'
            cursor = connection.cursor( )
            cursor.execute( nSqlone, [taskid])
            rows = cursor.fetchall()
            cursor.close()
            return rows
        elif rowdata == '2':
            nSqlone = 'select task_id,update_type,user_name,db_name,sql_data,c.db_id as db_id  from sql_update_task_info a join user_info b on a.user_id=b.user_id join db_data_info c on a.db_id=c.db_id where a.task_id=%s order by submit_time desc'
            cursor = connection.cursor( )
            cursor.execute( nSqlone, [taskid] )
            rows = cursor.fetchall()
            cursor.close()
            return rows

    @classmethod
    def updatemysqlsqltask(self,dbid,sqlcontent,nUserid,taskid):

        nSql = 'select outer_net,inner_net,use_outer_inner,db_port,db_user,db_allpri_pwd,defaults_db_name from db_data_info a join server_data_info b on a.server_id=b.server_id  where a.db_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSql, [dbid] )
        rows = cursor.fetchall( )
        for nNum in rows:
            nOuternet = nNum[0]
            nInnernet = nNum[1]
            nUseoutinner = nNum[2]
            nDbport = nNum[3]
            nDBuser = nNum[4]
            nDballpripwd = nNum[5]
            nDefaultdbname = nNum[6]

        if nUseoutinner == 1:
            nNet = nOuternet
        elif nUseoutinner == 2:
            nNet = nInnernet

        nTaskSql = "update sql_update_task_info set sql_data=%s where task_id=%s"
        cursor = connection.cursor( )
        cursor.execute(nTaskSql, [sqlcontent,taskid])
        cursor.close( )
        connection.commit()
        connection.close( )
        cursor = connection.cursor( )

    @classmethod
    def mysqlincepexecute(self, nUserid,taskid,userrole):
        nSqldata = 'select outer_net,inner_net,use_outer_inner,db_port,db_user,db_allpri_pwd,defaults_db_name,sql_data from db_data_info a join server_data_info b on a.server_id=b.server_id join sql_update_task_info c on a.db_id=c.db_id  where c.task_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSqldata, [taskid] )
        rows = cursor.fetchone( )

        nOuternet = rows[0]
        nInnernet = rows[1]
        nUseoutinner = rows[2]
        nDbport = rows[3]
        nDBuser = rows[4]
        nDballpripwd = rows[5]
        nDefaultdbname = rows[6]
        nUpdatesql= rows[7]

        if nUseoutinner == 1:
            nNet = nOuternet
        elif nUseoutinner == 2:
            nNet = nInnernet

        nIncepsql = '/*--user=%s;--password=%s;--host=%s;--enable-execute;--port=%d;*/' % (nDBuser, nDballpripwd, nNet, nDbport) + '\n' \
                        + 'inception_magic_start;' + '\n' \
                        + nUpdatesql + '\n' \
                        + 'inception_magic_commit;'

        nIncepsql = nIncepsql.encode( 'utf-8' ).decode( 'latin-1' )

        conn = MySQLdb.connect( host='hostname', user='user', passwd='pwd', db='mysql', port=6669,charset="utf8" )
        cursor = conn.cursor( )
        cursor.execute( nIncepsql )
        result = cursor.fetchall( )
        cursor.close( )
        conn.close( )
        for row in result:
            nCheckid = row[0]
            nCheckstage = row[1]
            nErrlevel = row[2]
            nStagestatus = row[3]
            nErrormessage = row[4].encode('utf8')
            nChecksql = row[5].encode( 'utf8' )
            nAffectedrows = row[6]

            checkSql = 'insert into sql_update_task_result (task_id,execute_id,execute_type,check_stage,err_level,stage_status,error_messge,check_sql,affected_row) values (%s,%s,2,%s,%s,%s,%s,%s,%s)'
            cursor = connection.cursor()
            cursor.execute( checkSql, [taskid, nCheckid, nCheckstage, nErrlevel, nStagestatus, nErrormessage, nChecksql,nAffectedrows] )
            cursor.close()
            connection.commit()
            connection.close()

        updatetypesql = 'update sql_update_task_info set task_type=1,is_inception_use=2,execute_user_id=%s where task_id=%s'
        cursor = connection.cursor()
        cursor.execute(updatetypesql, [nUserid,taskid])
        cursor.close()
        connection.commit()
        connection.close()

    @classmethod
    def mysqlsqlexecute(self, nUserid, taskid, userrole):
        nSqldata = 'select outer_net,inner_net,use_outer_inner,db_port,db_user,db_allpri_pwd,defaults_db_name,sql_data from db_data_info a join server_data_info b on a.server_id=b.server_id join sql_update_task_info c on a.db_id=c.db_id  where c.task_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSqldata, [taskid] )
        rows = cursor.fetchone( )
        print rows

        nOuternet = rows[0]
        nInnernet = rows[1]
        nUseoutinner = rows[2]
        nDbport = rows[3]
        nDBuser = rows[4]
        nDballpripwd = rows[5]
        nDefaultdbname = rows[6]
        nUpdatesql = rows[7].encode( encoding='UTF-8' )

        if nUseoutinner == 1:
            nNet = nOuternet
        elif nUseoutinner == 2:
            nNet = nInnernet

        try:
            conn = MySQLdb.connect( host=nNet, user=nDBuser, passwd=nDballpripwd, db=nDefaultdbname, port=nDbport,
                                    charset='utf8' )
            cursor = conn.cursor( )
            cursor.execute( nUpdatesql )
            cursor.close( )
            conn.commit( )
            resultdata = cursor.rowcount

        except MySQLdb.Error, e:
            resultdata = "Mysql Error %d: %s" % (e.args[0], e.args[1])

        print resultdata

        updatetypesql = 'update sql_update_task_info set task_type=1,is_inception_use=1,execute_user_id=%s where task_id=%s'
        cursor = connection.cursor( )
        cursor.execute( updatetypesql, [nUserid, taskid] )
        cursor.close( )
        connection.commit( )

        updatesqlresult = 'insert into  sql_update_task_result (task_id,execute_id,execute_type,check_sql,sql_execute_info) values (%s,1,1,%s,%s)'
        cursor = connection.cursor( )
        cursor.execute( updatesqlresult, [taskid, nUpdatesql,resultdata] )
        cursor.close( )
        connection.commit( )

    @classmethod
    def deletemysqltask(self, nUserid, taskid):
        nSql = 'delete from sql_update_task_info  where task_id=%s and task_type=0' % (taskid)
        cursor = connection.cursor( )
        cursor.execute( nSql )
        connection.commit( )
        cursor.close( )
        connection.close( )

    @classmethod
    def mysqlcheckdata(self,nUserid,taskid):
        nSql = 'select task_id,check_id,check_stage,err_level,stage_status,error_messge,check_sql,affected_row from sql_check_task_info where task_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSql, [taskid] )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def mysqlexecuteresult(self, nUserid, taskid,executetype):
        if executetype ==2:
            nSql = 'select task_id,execute_id,execute_type,check_stage,err_level,stage_status,error_messge,check_sql,affected_row,sql_execute_info from sql_update_task_result where task_id=%s'
            cursor = connection.cursor( )
            cursor.execute( nSql, [taskid])
            rows = cursor.fetchall( )
            cursor.close( )
            return rows
        elif executetype ==1:
            nSql = 'select task_id,execute_id,execute_type,sql_execute_info,sql_execute_info from sql_update_task_result where task_id=%s'
            cursor = connection.cursor( )
            cursor.execute( nSql, [taskid] )
            rows = cursor.fetchall( )
            cursor.close( )
            return rows

    @classmethod
    def mysqlfinishtask(self, userid, userrole):
        if userrole == 1:
            nSql = 'select task_id,b.user_name as submit_user_name,db_name,task_type,update_type,submit_time,is_inception_use,e.user_name as execute_user_name,execute_time from sql_update_task_info a left join user_info b on a.user_id=b.user_id left join db_data_info c on a.db_id=c.db_id left join server_data_info d on c.server_id=d.server_id left join user_info e on a.execute_user_id=e.user_id  where task_type=1 and task_style=0 order by execute_time desc'
        else:
            nSql = 'select task_id,b.user_name as submit_user_name,db_name,task_type,update_type,submit_time,is_inception_use,e.user_name as execute_user_name,execute_time from sql_update_task_info a left join user_info b on a.user_id=b.user_id left join db_data_info c on a.db_id=c.db_id left join server_data_info d on c.server_id=d.server_id left join user_info e on a.execute_user_id=e.user_id where a.user_id=%s and task_type=1 and task_style=0  order by execute_time desc' % (userid)
        cursor = connection.cursor( )
        cursor.execute( nSql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def mysqlunfinishtasknum(self, userid,userrole):
        if userrole ==1 :
            nSql = 'select count(*) as num from  sql_update_task_info b where task_type=0'
        else:
            nSql = 'select count(*) as num from user_info a join sql_update_task_info b on a.user_id=b.user_id  where a.user_id=%s and task_type=0' %(userid)

        cursor = connection.cursor( )
        cursor.execute( nSql)
        rows = cursor.fetchall( )
        cursor.close( )
        for nNum in rows:
            return nNum

    @classmethod
    def mysqlfinishtasknum(self, userid,userrole):
        if userrole == 1:
            nSql = 'select count(*) as num from  sql_update_task_info  where  task_type=1'
        else:
            nSql = 'select count(*) as num from user_info a join sql_update_task_info b on a.user_id=b.user_id  where a.user_id=%s and task_type=1' %(userid)
        cursor = connection.cursor( )
        cursor.execute( nSql )
        rows = cursor.fetchall( )
        cursor.close( )
        for nNum in rows:
            return nNum

    @classmethod
    def mysqlexecutetype(self, nUserid, taskid):
        nSql = 'select is_inception_use from sql_update_task_info where task_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nSql, [taskid] )
        rows = cursor.fetchone( )
        return rows[0]


