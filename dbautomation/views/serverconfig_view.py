#!/usr/bin/env python
#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from dbautomation.model.serverconfig_model import ServerConfig


def serverdatalist(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        serverinfolist = ServerConfig.serverdatalist()
        print len(serverinfolist)
        return render_to_response( 'serverdatalist.html', {'datas': serverinfolist,'num3': nUserrole})

def addserverdata(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nServerid = req.POST.get( 'serverid' )
            nUserrole = req.session["sess_userrole"]
            return render_to_response( 'addserverdata.html',{'num3': nUserrole})
    else:
        nServername = req.POST.get('servername')
        nFuncname = req.POST.get( 'funcname' )
        nMemerynum = req.POST.get('memerynum')
        nCpunum = req.POST.get( 'cpunum' )
        nInnernet = req.POST.get( 'innernet' )
        nOutnet = req.POST.get( 'outnet' )
        nUseouterinner = req.POST.get( 'useouterinner' )
        nSshport = req.POST.get( 'sshport' )
        nServercontent = req.POST.get( 'servercontent' )
        nUserid = req.session["sess_userid"]
        ServerConfig.addserverdata( nServername,nFuncname,nMemerynum,nCpunum,nInnernet,nOutnet,nUseouterinner,nSshport,nServercontent)
        return HttpResponseRedirect('/serverdatalist/')

def updateserverdata(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nServerid = req.GET['serverid']
            serverinfolist = ServerConfig.beforupdateserverdata( nServerid )
            return render_to_response( 'updateserverdata.html', {'datas': serverinfolist} )
    else:
        nUserid = req.session["sess_userid"]
        nServerid = req.POST.get('serverid')
        nServername = req.POST.get( 'servername' )
        nFuncname = req.POST.get( 'funcname' )
        nMemerynum = req.POST.get( 'memerynum' )
        nCpunum = req.POST.get( 'cpunum' )
        nInnernet = req.POST.get( 'innernet' )
        nOutnet = req.POST.get( 'outnet' )
        nUseouterinner = req.POST.get( 'useouterinner' )
        nSshport = req.POST.get( 'sshport' )
        nServercontent = req.POST.get( 'servercontent' )
        print nServerid
        ServerConfig.updateserverdata(nServerid,nServername,nFuncname,nMemerynum,nCpunum,nInnernet,nOutnet,nUseouterinner,nSshport,nServercontent)
        return HttpResponseRedirect( '/serverdatalist/' )

def deleteserverdata(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nserverid= req.GET['serverid']
        nUserid = req.session["sess_userid"]
        ServerConfig.deleteserverdata(nserverid)
        return HttpResponseRedirect('/serverdatalist/')

def dbdatalist(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        serverinfolist = ServerConfig.dbdatalist()
        return render_to_response( 'dbdatalist.html', {'datas': serverinfolist,'num3': nUserrole})

def adddbdata(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nServerid = req.POST.get('serverid')
            nUserrole = req.session["sess_userrole"]
            serverinfolist = ServerConfig.selectserverdata( )
            return render_to_response( 'adddbdata.html',{'datas': serverinfolist,'num3': nUserrole})
    else:
        nServerid = req.POST.get('serverid')
        nDbname = req.POST.get( 'dbname' )
        nDbtype = req.POST.get('dbtype')
        nDbrole = req.POST.get('dbrole')
        nDefaultsdbname = req.POST.get('defaultsdbname')
        nDbport = req.POST.get('dbport')
        nDbuser = req.POST.get('dbuser')
        nDbpassword = req.POST.get('dbpassword')
        nDbcontent = req.POST.get('dbcontent')
        nUserid = req.session["sess_userid"]
        ServerConfig.adddbdata( nServerid,nDbname,nDbtype,nDbrole,nDefaultsdbname,nDbport,nDbuser,nDbpassword,nDbcontent)
        return HttpResponseRedirect('/dbdatalist/')

def updatedbdata(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nDbid = req.GET['dbid']
            nUserrole = req.session["sess_userrole"]
            serverinfolist = ServerConfig.beforupdatedbdata( nDbid )
            return render_to_response( 'updatedbdata.html', {'datas': serverinfolist,'num3': nUserrole} )
    else:
        nUserid = req.session["sess_userid"]
        nDbid = req.POST.get('dbid')
        nServerid = req.POST.get('serverid')
        nDbname = req.POST.get( 'dbname' )
        nDbtype = req.POST.get( 'dbtype' )
        nDbrole = req.POST.get( 'dbrole' )
        nDefaultsdbname = req.POST.get( 'defaultsdbname' )
        nDbport = req.POST.get( 'dbport' )
        nDbuser = req.POST.get( 'dbuser' )
        nDbpassword = req.POST.get( 'dbpassword' )
        nDbcontent = req.POST.get( 'dbcontent' )
        print nServerid
        ServerConfig.updatedbdata(nServerid,nDbname,nDbtype,nDbrole,nDefaultsdbname,nDbport,nDbuser,nDbpassword,nDbcontent,nDbid)
        return HttpResponseRedirect( '/dbdatalist/' )

def deletedbdata(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nDbid= req.GET['dbid']
        nUserid = req.session["sess_userid"]
        ServerConfig.deletedbdata(nDbid)
        return HttpResponseRedirect('/dbdatalist/')


def userdatalist(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        serverinfolist = ServerConfig.userdatalist()
        return render_to_response( 'userdatalist.html', {'datas': serverinfolist,'num1':nUserid,'num3': nUserrole})

def adduserdata(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            serverinfolist = ServerConfig.selectdbdata( )
            return render_to_response( 'adduserdata.html',{'datas': serverinfolist,'num3': nUserrole})
    else:
        nUserid = req.session["sess_userid"]
        nLoginname = req.POST.get( 'loginname' )
        nLoginpwd = req.POST.get( 'loginpwd' )
        nUsername = req.POST.get( 'username' )
        nUseremail = req.POST.get( 'useremail' )
        nUsermobile = req.POST.get( 'usermobile' )
        nUserrole = req.POST.get( 'userrole' )
        nUserdepartment = req.POST.get( 'userdepartment' )
        nIsforbiden = req.POST.get( 'isforbiden' )
        ServerConfig.adduserdata(nLoginname,nLoginpwd,nUsername,nUseremail,nUsermobile,nUserrole,nUserdepartment,nIsforbiden)
        return HttpResponseRedirect( '/userdatalist/' )

def updateuserdata(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nNewuserid = req.GET['userid']
            nUserrole = req.session["sess_userrole"]
            serverinfolist = ServerConfig.beforupdateuserdata( nNewuserid )
            return render_to_response( 'updateuserdata.html', {'datas': serverinfolist,'num3': nUserrole} )
    else:
        nUserid = req.session["sess_userid"]
        nNewuserid = req.POST.get( 'userid' )
        nLoginname = req.POST.get('loginname')
        nLoginpwd = req.POST.get('loginpwd')
        nUsername = req.POST.get( 'username' )
        nUseremail = req.POST.get( 'useremail' )
        nUsermobile = req.POST.get( 'usermobile' )
        nUserrole = req.POST.get( 'userrole' )
        nUserdepartment = req.POST.get( 'userdepartment' )
        nIsforbiden = req.POST.get( 'isforbiden' )
        ServerConfig.updateuserdata(nLoginname,nLoginpwd,nUsername,nUseremail,nUsermobile,nUserrole,nUserdepartment,nIsforbiden,nNewuserid)
        return HttpResponseRedirect( '/userdatalist/' )

def deleteuserdata(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nNewUserid= req.GET['userid']
        nUserid = req.session["sess_userid"]
        ServerConfig.deleteuserdata(nNewUserid)
        return HttpResponseRedirect('/userdatalist/')

def useuserdata(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nNewUserid= req.GET['userid']
        nUserid = req.session["sess_userid"]
        ServerConfig.useuserdata(nNewUserid)
        return HttpResponseRedirect('/userdatalist/')


def adduserpri(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            npriuser = req.GET["userid"]
            nUserrole = req.session["sess_userrole"]
            dblist = ServerConfig.selectdbdata()
            return render_to_response( 'adduserpri.html',{'datas': dblist,'num3': nUserrole,'num1': npriuser})
    else:
        nUserid = req.session["sess_userid"]
        nDbid = req.POST.get( 'dbid' )
        npriuser = req.POST.get('userid')
        ServerConfig.adduserpri(nDbid,npriuser)
        return HttpResponseRedirect( '/userdatalist/' )

def deleteuserpri(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            npriuser = req.GET["userid"]
            nUserrole = req.session["sess_userrole"]
            dblist = ServerConfig.selectdbdata()
            return render_to_response( 'deleteuserpri.html',{'datas': dblist,'num3': nUserrole,'num1': npriuser})
    else:
        nUserid = req.session["sess_userid"]
        nDbid = req.POST.get( 'dbid' )
        npriuser = req.POST.get('userid')
        ServerConfig.deleteuserpri(nDbid,npriuser)
        return HttpResponseRedirect( '/userdatalist/' )
