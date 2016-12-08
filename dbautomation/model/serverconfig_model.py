#!/usr/bin/env python
#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.db import connection

class ServerConfig(object):
    def __init__(self, nServerid,nMemerynum,nCpunum,nInnernet,nOutnet,nUseouterinner,nSshport,nServercontent,nServername,nFuncname,nDbname,nDbtype,
                 nDbrole,nDefaultsdbname,nDbport,nDbuser,nDbpassword,nDbcontent,nDbid,nLoginname,nLoginpwd,nUsername,nUseremail,nUsermobile,nUserrole,nUserdepartment,nIsforbiden,npriuser):
        self.nServerid = nServerid
        self.nMemerynum = nMemerynum
        self.nCpunum = nCpunum
        self.nInnernet = nInnernet
        self.nOutnet = nOutnet
        self.nUseouterinner = nUseouterinner
        self.nServercontent = nServercontent
        self.nFuncname = nFuncname
        self.nSshport = nSshport
        self.nDbname = nDbname
        self.nDbtype = nDbtype
        self.nDbrole = nDbrole
        self.nDefaultsdbname = nDefaultsdbname
        self.nDbport = nDbport
        self.nDbuser = nDbuser
        self.nDbpassword = nDbpassword
        self.nDbcontent = nDbcontent
        self.nDbid = nDbid
        self.nLoginname = nLoginname
        self.nLoginpwd = nLoginpwd
        self.nUsername = nUsername
        self.nUseremail = nUseremail
        self.nUsermobile = nUsermobile
        self.nUserrole = nUserrole
        self.nUserdepartment = nUserdepartment
        self.nIsforbiden = nIsforbiden
        self.npriuser = str(npriuser)

    @classmethod
    def serverdatalist(self):
        nsql='select server_id,server_name,outer_net,inner_net,func_name,use_outer_inner from server_data_info '
        cursor = connection.cursor()
        cursor.execute(nsql)
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def addserverdata(self,nServername,nFuncname,nMemerynum,nCpunum,nInnernet,nOutnet,nUseouterinner,nSshport,nServercontent):
        nsql = 'insert into server_data_info (server_name,func_name,memory_data,cpu_data,inner_net,outer_net,use_outer_inner,ssh_port,content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nServername,nFuncname,nMemerynum,nCpunum,nInnernet,nOutnet,nUseouterinner,nSshport,nServercontent])
        cursor.close( )
        connection.commit( )
        connection.close( )

    @classmethod
    def updateserverdata(self, nServerid,nServername,nFuncname,nMemerynum,nCpunum,nInnernet,nOutnet,nUseouterinner,nSshport,nServercontent):
        nsql = 'update server_data_info set server_name=%s,func_name=%s,memory_data=%s,cpu_data=%s,inner_net=%s,outer_net=%s,use_outer_inner=%s,ssh_port=%s,content=%s where server_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nServername,nFuncname,nMemerynum,nCpunum,nInnernet,nOutnet,nUseouterinner,nSshport,nServercontent,nServerid] )
        connection.commit( )
        cursor.close( )
        connection.close( )

    @classmethod
    def deleteserverdata(self, nServerid):
        nsql = 'delete a.*,b.*,c.* from server_data_info a left join db_data_info b on a.server_id=b.server_id left join user_db_relation c on b.db_id=c.db_id where a.server_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql,[nServerid] )
        connection.commit( )
        cursor.close( )
        connection.close( )

    @classmethod
    def beforupdateserverdata(self, nServerid):
        nsql = 'select server_id,server_name,func_name,memory_data,cpu_data,inner_net,outer_net,use_outer_inner,ssh_port,content from server_data_info where server_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nServerid] )
        row = cursor.fetchone( )
        cursor.close( )
        return row

    @classmethod
    def dbdatalist(self):
        nsql = 'select a.db_id as db_id,server_name,outer_net,inner_net,db_name,db_type,db_port from  db_data_info a  join server_data_info b on a.server_id=b.server_id '
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def adddbdata(self,nServerid,nDbname,nDbtype,nDbrole,nDefaultsdbname,nDbport,nDbuser,nDbpassword,nDbcontent):
        nsql = 'insert into db_data_info (server_id,db_name,db_type,db_role,defaults_db_name,db_port,db_user,db_allpri_pwd,content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor = connection.cursor()
        cursor.execute( nsql,[nServerid,nDbname,nDbtype,nDbrole,nDefaultsdbname,nDbport,nDbuser,nDbpassword,nDbcontent])
        dbiddata = cursor.lastrowid
        cursor.close()
        connection.commit( )

        relatsql = 'insert into user_db_relation  select user_id,%s,now(),now() from user_info where user_role=1'
        cursor = connection.cursor( )
        cursor.execute( relatsql, [dbiddata] )
        cursor.close( )
        connection.commit( )

    @classmethod
    def selectserverdata(self):
        nsql = 'select server_id,server_name from  server_data_info '
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def beforupdatedbdata(self, nDbid):
        nsql = 'select a.server_id,server_name,db_id,db_name,db_type,db_role,db_port,db_user,db_allpri_pwd,defaults_db_name,a.content from db_data_info a  join server_data_info b on a.server_id=b.server_id where db_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nDbid] )
        row = cursor.fetchone( )
        cursor.close( )
        return row

    @classmethod
    def updatedbdata(self, nServerid,nDbname,nDbtype,nDbrole,nDefaultsdbname,nDbport,nDbuser,nDbpassword,nDbcontent,nDbid):
        nsql = 'update db_data_info set server_id=%s,db_name=%s,db_type=%s,db_role=%s,defaults_db_name=%s,db_port=%s,db_user=%s,db_allpri_pwd=%s,content=%s where db_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql,[nServerid,nDbname,nDbtype,nDbrole,nDefaultsdbname,nDbport,nDbuser,nDbpassword,nDbcontent,nDbid] )
        connection.commit( )
        cursor.close( )
        connection.close( )

    @classmethod
    def deletedbdata(self, nDbid):
        nsql = 'delete b.*,c.* from  db_data_info b left join user_db_relation c on b.db_id=c.db_id where b.db_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nDbid] )
        connection.commit( )
        cursor.close( )
        connection.close( )

    @classmethod
    def userdatalist(self):
        nsql = 'select a.user_id,login_name,user_name,user_email,user_mobile,user_role,user_department, group_concat(db_name),is_forbid from  user_info a left join  user_db_relation b  on a.user_id=b.user_id left join db_data_info c on b.db_id=c.db_id group by a.user_id'
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def selectdbdata(self):
        nsql = 'select db_id,db_name from  db_data_info '
        cursor = connection.cursor( )
        cursor.execute( nsql )
        rows = cursor.fetchall( )
        cursor.close( )
        return rows

    @classmethod
    def adduserdata(self, nLoginname,nLoginpwd,nUsername,nUseremail,nUsermobile,nUserrole,nUserdepartment,nIsforbiden):
        nsql = 'insert into user_info (login_name,login_pwd,user_name,user_email,user_mobile,user_role,user_department,is_forbid) values (%s,md5(%s),%s,%s,%s,%s,%s,%s)'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nLoginname,nLoginpwd,nUsername,nUseremail,nUsermobile,nUserrole,nUserdepartment,nIsforbiden] )
        useriddata = cursor.lastrowid
        cursor.close( )
        connection.commit( )

        if nUserrole == 1:
            relatsql = 'insert into user_db_relation  select %s,db_id,now(),now() from db_data_info'
            cursor = connection.cursor( )
            cursor.execute( relatsql, [useriddata] )
            cursor.close( )
            connection.commit( )

    @classmethod
    def beforupdateuserdata(self, nUserid):
        nsql = 'select user_id,login_name,login_pwd,user_name,user_email,user_mobile,user_role,user_department,is_forbid from user_info where user_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nUserid] )
        row = cursor.fetchone( )
        cursor.close( )
        return row

    @classmethod
    def updateuserdata(self, nLoginname,nLoginpwd,nUsername,nUseremail,nUsermobile,nUserrole,nUserdepartment,nIsforbiden,nUserid):
        nsql = 'update user_info set login_name=%s,login_pwd=%s,user_name=%s,user_email=%s,user_mobile=%s,user_role=%s,user_department=%s,is_forbid=%s where user_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nLoginname,nLoginpwd,nUsername,nUseremail,nUsermobile,nUserrole,nUserdepartment,nIsforbiden,nUserid] )
        connection.commit( )
        cursor.close( )
        connection.close( )

        if nUserrole == '1':
            relatsql = 'replace into user_db_relation  select %s,db_id,now(),now() from db_data_info'
            cursor = connection.cursor( )
            cursor.execute( relatsql, [nUserid] )
            cursor.close( )
            connection.commit( )

    @classmethod
    def deleteuserdata(self, nUserid):
        nsql = 'update  user_info set is_forbid=0 where user_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nUserid] )
        connection.commit( )
        cursor.close( )
        connection.close( )

    @classmethod
    def useuserdata(self, nUserid):
        nsql = 'update  user_info set is_forbid=1 where user_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql, [nUserid] )
        connection.commit( )
        cursor.close( )
        connection.close( )

    @classmethod
    def adduserpri(self,nDbid,npriuser):
        nsql = 'replace into user_db_relation (user_id,db_id) values (%s,%s)'
        cursor = connection.cursor( )
        cursor.execute( nsql, [npriuser,nDbid] )
        cursor.close( )
        connection.commit( )

    @classmethod
    def deleteuserpri(self, nDbid,npriuser):
        nsql = 'delete from user_db_relation where db_id=%s and user_id=%s'
        cursor = connection.cursor( )
        cursor.execute( nsql,[nDbid,npriuser])
        connection.commit( )
        cursor.close( )
        connection.close( )