#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from dbautomation.model.sqlupdate_model import SqlUpdate
from dbautomation.model.monitor_model import Monitor

def mysqlmonitor(req):
    if not req.session.get("sess_username", False):
        return HttpResponseRedirect("/index/")
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        dbinfolist = SqlUpdate.mysqlinfolist( nUserid )
        unfinishnum = SqlUpdate.mysqlunfinishtasknum( nUserid, nUserrole )
        finishnum = SqlUpdate.mysqlfinishtasknum( nUserid, nUserrole )

        return render_to_response('mysqlmonitor.html',{'datas': dbinfolist, 'num1': unfinishnum, 'num2': finishnum, 'num3': nUserrole})

def portmonitorlist(req):
    if not req.session.get("sess_username", False):
        return HttpResponseRedirect("/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        datalist = Monitor.portmonitorlist()
        return render_to_response('portmonitorlist.html',{'datas': datalist,'num3': nUserrole} )


def addportmonitor(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/", "需要登录才可以访问" )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            datalist = Monitor.getbeforaddportmonitor()
            return render_to_response( 'addportmonitor.html', {'datas': datalist,'num3': nUserrole} )
    else:
        nUserid = req.session["sess_userid"]
        nServerid = req.POST.get('serverid')
        nMonitortype= req.POST.get('monitortype')
        nMonitorname = req.POST.get('monitorname')
        nMonitorvalue = req.POST.get('monitorvalue')
        nIsmonitor = req.POST.get('ismonitor')
        Monitor.addportmonitor( nUserid,nServerid,nMonitortype,nMonitorname,nMonitorvalue,nIsmonitor)
        return HttpResponseRedirect('/portmonitorlist/')

def updateportmonitor(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/", "需要登录才可以访问" )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            nMonitorid = req.GET["monitorid"]
            datalist = Monitor.getbeforupdateservermonitor(nMonitorid)
            return render_to_response( 'updateportmonitor.html', {'datas': datalist} )
    else:
        nUserid = req.session["sess_userid"]
        nServerid = req.POST.get( 'serverid' )
        nMonitorid= req.POST.get( 'monitorid' )
        nMonitortype= req.POST.get( 'monitortype' )
        nMonitorname = req.POST.get( 'monitorname' )
        nMonitorvalue = req.POST.get( 'monitorvalue' )
        nIsmonitor = req.POST.get( 'ismonitor' )
        print nMonitortype

        Monitor.updateportmonitor( nMonitorid,nServerid,nMonitortype,nMonitorname,nMonitorvalue,nIsmonitor)
        return HttpResponseRedirect( '/portmonitorlist/' )

def deleteportmonitor(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nMonitorid = req.GET["monitorid"]
        Monitor.deleteportmonitor(nMonitorid)
        return HttpResponseRedirect( '/portmonitorlist/' )



def dbmonitorlist(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        datalist = Monitor.dbmonitorlist()
        return render_to_response( 'dbmonitorlist.html',{'datas': datalist,'num3': nUserrole} )

def adddbmonitor(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/", "需要登录才可以访问" )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            datalist = Monitor.getbeforadddbmonitor()
            return render_to_response( 'adddbmonitor.html', {'datas': datalist,'num3': nUserrole} )
    else:
        nUserid = req.session["sess_userid"]
        nDbid = req.POST.get( 'dbid' )
        nMonitortype= req.POST.get( 'monitortype' )
        nMonitorname = req.POST.get( 'monitorname' )
        nMonitorshell = req.POST.get( 'monitorshell' )
        nIsmonitor = req.POST.get( 'ismonitor' )

        Monitor.adddbmonitor( nUserid,nMonitortype,nMonitorname,nMonitorshell,nIsmonitor)
        return HttpResponseRedirect( '/dbmonitorlist/' )

def updatedbmonitor(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/", "需要登录才可以访问" )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            nMonitorid = req.GET["monitorid"]
            datalist = Monitor.getbeforupdatedbmonitor(nMonitorid)
            return render_to_response( 'updatedbmonitor.html', {'datas': datalist} )
    else:
        nUserid = req.session["sess_userid"]
        nDbid = req.POST.get('dbid')
        nMonitorid= req.POST.get('monitorid')
        nMonitortype= req.POST.get('monitortype')
        nMonitorname = req.POST.get('monitorname')
        nMonitorshell = req.POST.get('monitorshell')
        nIsmonitor = req.POST.get('ismonitor')

        Monitor.updatedbmonitor( nMonitorid,nMonitortype,nMonitorname,nMonitorshell,nIsmonitor)
        return HttpResponseRedirect('/dbmonitorlist/')

def deletedbmonitor(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nMonitorid = req.GET["monitorid"]
        Monitor.deleteportmonitor(nMonitorid)
        return HttpResponseRedirect('/dbmonitorlist/')



def osmonitorlist(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        datalist = Monitor.osmonitorlist()
        return render_to_response( 'osmonitorlist.html',{'datas': datalist,'num3': nUserrole} )

def addosmonitor(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/", "需要登录才可以访问" )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            datalist = Monitor.getbeforaddosmonitor()
            return render_to_response( 'addosmonitor.html', {'datas': datalist,'num3': nUserrole} )
    else:
        nUserid = req.session["sess_userid"]
        nMonitortype= req.POST.get( 'monitortype' )
        nMonitorname = req.POST.get( 'monitorname' )
        nMonitorshell = req.POST.get( 'monitorshell' )
        nIsmonitor = req.POST.get( 'ismonitor' )

        Monitor.addosmonitor( nUserid,nMonitortype,nMonitorname,nMonitorshell,nIsmonitor)
        return HttpResponseRedirect('/osmonitorlist/')

def updateosmonitor(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/", "需要登录才可以访问" )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            nMonitorid = req.GET["monitorid"]
            datalist = Monitor.getbeforupdateservermonitor(nMonitorid)
            return render_to_response( 'updateosmonitor.html', {'datas': datalist} )
    else:
        nUserid = req.session["sess_userid"]
        nMonitorid= req.POST.get('monitorid')
        nMonitortype= req.POST.get('monitortype')
        nMonitorname = req.POST.get('monitorname')
        nMonitorshell = req.POST.get('monitorshell')
        nIsmonitor = req.POST.get('ismonitor')

        Monitor.updateosmonitor( nMonitorid,nMonitortype,nMonitorname,nMonitorshell,nIsmonitor)
        return HttpResponseRedirect('/osmonitorlist/')

def deleteosmonitor(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nMonitorid = req.GET["monitorid"]
        Monitor.deleteportmonitor(nMonitorid)
        return HttpResponseRedirect('/osmonitorlist/')


def adddbmonitorrelation(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/")
        else:
            username = req.session["sess_username"]
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            datalist = SqlUpdate.mysqlinfolist(nUserid)
            datalist1 = Monitor.getbeforadddbmonitorrelation( )
            return render_to_response( 'adddbmonitorrelation.html', {'datas': datalist, 'data1': datalist1,'num3': nUserrole} )
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nDbid = req.POST.get("dbid")
        nMonitorid = req.POST.get("monitorid")
        print nDbid,nMonitorid
        datalist = Monitor.adddbmonitorrealtion(nDbid,nMonitorid)
        return HttpResponseRedirect( '/dbmonitorrelationlist/' )

def dbmonitorrelationlist(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/" )
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        datalist = Monitor.dbmonitorrelationlist()
        print datalist
        return render_to_response( 'dbmonitorrelationlist.html', {'datas': datalist, 'num3': nUserrole})

def deletedbmonitorrealtion(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nMonitorid = req.GET["monitorid"]
        nDbid = req.GET["dbid"]
        print nMonitorid,nDbid
        Monitor.deletedbmonitorrealtion(nDbid,nMonitorid)
        return HttpResponseRedirect('/dbmonitorrelationlist/')


def addosmonitorrelation(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/")
        else:
            username = req.session["sess_username"]
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            datalist = Monitor.getbeforaddosmonitor()
            datalist1 = Monitor.getbeforaddosmonitorrelation()
            return render_to_response( 'addosmonitorrelation.html', {'datas': datalist, 'data1': datalist1,'num3': nUserrole} )
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nServerid = req.POST.get("serverid")
        nMonitorid = req.POST.get("monitorid")
        print nServerid,nMonitorid
        datalist = Monitor.addosmonitorrealtion(nServerid,nMonitorid)
        return HttpResponseRedirect( '/osmonitorrelationlist/' )

def osmonitorrelationlist(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/" )
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        datalist = Monitor.osmonitorrelationlist()
        return render_to_response( 'osmonitorrelationlist.html', {'datas': datalist, 'num3': nUserrole})

def deleteosmonitorrealtion(req):
    if not req.session.get( "sess_username", False ):
        return HttpResponseRedirect( "/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nMonitorid = req.GET["monitorid"]
        nServerid = req.GET["serverid"]
        Monitor.deleteosmonitorrealtion(nServerid,nMonitorid)
        return HttpResponseRedirect('/osmonitorrelationlist/')