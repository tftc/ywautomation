#!/usr/bin/env python
# -*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,render
from dbautomation.model.sqlupdate_model import SqlUpdate

# mysql数据库信息详情
def mysqldata(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        dbinfolist=SqlUpdate.mysqlinfolist(nUserid)
        unfinishnum=SqlUpdate.mysqlunfinishtasknum(nUserid,nUserrole)
        finishnum = SqlUpdate.mysqlfinishtasknum(nUserid,nUserrole)

        return render_to_response('mysqldata.html', {'datas': dbinfolist,'num1': unfinishnum,'num2': finishnum,'num3': nUserrole})

def mysqlsqltask(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            dbinfolist = SqlUpdate.mysqlinfolist( nUserid )
            return render_to_response( 'mysqlsqltask.html',{'datas': dbinfolist,'num3': nUserrole})
    else:
            nUserid = req.session["sess_userid"]
            nDbid = req.POST.get('dbid')
            nSqlContent = req.POST.get('sqlcontent').encode('utf-8')
            SqlUpdate.addmysqlsqltask(nDbid,nSqlContent,nUserid)
            return HttpResponseRedirect('/tobeexecutemysqltask/')

def tobeexecutemysqltask(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        dbinfolist = SqlUpdate.mysqlunexecutetask(nUserid,nUserrole)
        return render_to_response( 'tobeexecutemysqltask.html', {'datas': dbinfolist,'num3': nUserrole})

def deletemysqltask(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nTaskid = req.GET['id']
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        SqlUpdate.deletemysqltask(nUserid,nTaskid)
        return HttpResponseRedirect( '/tobeexecutemysqltask/' )


def mysqlsqlexecute(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nTaskid = req.GET['id']
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        SqlUpdate.mysqlsqlexecute(nUserid,nTaskid,nUserrole)
        return HttpResponseRedirect( '/mysqlfinishtask/' )


def updatemysqlsqltask(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nTaskid = req.GET['id']
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            selecttaskdata = SqlUpdate.selectmysqlsqltask(nTaskid,nUserid)
            return render_to_response('updatemysqlsqltask.html', {'datas': selecttaskdata,'num3': nUserrole})
    else:
        nDbid = req.POST.get('dbid')
        nTaskid = req.POST.get('taskid')
        nUserid = req.session["sess_userid"]
        nSqlContent = req.POST.get('sqlcontent')
        SqlUpdate.updatemysqlsqltask(nDbid,nSqlContent,nUserid,nTaskid)
        return HttpResponseRedirect('/tobeexecutemysqltask/')

def mysqlsqlcontentinfo(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nTaskid = req.GET['id']
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        sqlinfodata = SqlUpdate.mysqlsqlcontentinfo(nTaskid)
        return render_to_response( 'mysqlsqlcontentinfo.html', {'datas': sqlinfodata,'num3': nUserrole})

def mysqlcheckdata(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nTaskid = req.GET['id']
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        sqlcheckdata = SqlUpdate.mysqlcheckdata(nUserid,nTaskid)
        return render_to_response( 'mysqlcheckdata.html', {'datas': sqlcheckdata,'num3': nUserrole})

def mysqlincepexecute(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nTaskid = req.GET['id']
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        SqlUpdate.mysqlincepexecute(nUserid,nTaskid,nUserrole)
        return HttpResponseRedirect('/mysqlfinishtask/')

def mysqlexecuteresult(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nTaskid = req.GET['id']
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nExecuttype=SqlUpdate.mysqlexecutetype(nUserid,nTaskid)
        sqlexecutedata = SqlUpdate.mysqlexecuteresult(nUserid,nTaskid,nExecuttype)
        return render_to_response( 'mysqlexecuteresult.html', {'num1': nExecuttype,'datas': sqlexecutedata,'num3': nUserrole} )

def mysqlfiletask(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            dbinfolist = SqlUpdate.mysqlinfolist( nUserid )
            return render_to_response( 'mysqlfiletask.html', {'datas': dbinfolist,'num3': nUserrole} )
    else:
        uuploaddata = req.POST.get('file')

        print uuploaddata['name']
        #SqlUpdate.addmysqlsqltask( nDbid, nIncepUse, nSqlContent )
        return HttpResponseRedirect( '/tobeexecutemysqltask/' )


def mediatables(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        return render_to_response( 'mediatables.html' )


def checkmysqltask(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        return render_to_response( 'inceptioncheckresult.html' )


def executemysqltask(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        return render_to_response( 'tobeexecutemysqltask.html')


def mysqlfinishtask(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        dbinfolist = SqlUpdate.mysqlfinishtask(nUserid, nUserrole)
        return render_to_response('finishmysqltask.html', {'datas': dbinfolist,'num3': nUserrole})
