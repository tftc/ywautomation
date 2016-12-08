#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from dbautomation.model.serverapply_model import Serverapply
import commands
import datetime
import MySQLdb

def serverapplylist(req):
    if not req.session.get("sess_username", False):
        return HttpResponseRedirect("/index/")
    else:
        username = req.session["sess_username"]
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        datalist = Serverapply.serverapplylist()
        return render_to_response('serverapplylist.html',{'datas': datalist,'num3': nUserrole} )


def addserverapply(req):
    if req.method == 'GET':
        if not req.session.get( "sess_username", False ):
            return HttpResponseRedirect( "/index/", "not login in " )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            return render_to_response( 'addserverapply.html' )
    else:
        nUserid = req.session["sess_userid"]
        nProjectname = req.POST.get( 'projectname' )
        nServerid = req.POST.get('serverip')
        nServerport= req.POST.get('serverport')
        nApplytype = req.POST.get('applytype')
        nApplyname = req.POST.get('applyname')
        nApplyport = req.POST.get('applyport')
        nApplytags = req.POST.get('applytag')

        Serverapply.addserverapply(nProjectname,nServerid,nServerport,nApplytype,nApplyname,nApplyport,nApplytags)
        return HttpResponseRedirect('/serverapplylist/')

def showserverapply(req):
    projectnamelist = Serverapply.getprojectname()
    alldata=[]
    for i in projectnamelist:
        serverapplydata = []
        nProjectname = i[0]

        applytypelist = Serverapply.getapplytype(nProjectname)
        for j in applytypelist:
            applytypedata = []
            nProjectname = j[0]
            nApplytype = j[1]

            applydatalist = Serverapply.getapplyname( nProjectname,nApplytype )
            numn=0
            for m in applydatalist:
                applydata = []
                nProjectname = m[0]
                nApplytype = m[1]
                nServerip = m[2]
                nServerport = m[3]
                nApplyname = m[4]
                nApplyport = m[5]
                nApplytag = m[6]
                applydata.append( nProjectname )
                applydata.append( nApplytype )
                applydata.append(nServerip)
                applydata.append(nServerport)
                applydata.append(nApplyname)
                applydata.append(nApplyport)
                applydata.append(nApplytag)

                nNum = 0
                shelldata = "ssh root@%s 'ps -ef|grep %s|grep -v grep|wc -l'" % (nServerip,nApplytag)
                nNum = commands.getoutput( shelldata )

                nNum1 = 0
                shelldata1 = 'nmap -p %s  %s |grep open|wc -l' % (nApplyport, nServerip)
                nNum1 = commands.getoutput( shelldata1 )
                nNum1 = nNum.strip( )

                numn+=1
                applydata.append(int(nNum))
                applydata.append(int(nNum1))
                applytypedata.append(applydata)
            serverapplydata.append(applytypedata)
        alldata.append(serverapplydata)
    print(alldata)
    #return HttpResponseRedirect( '/showserverapply/' )
    return render_to_response('showserverapply.html',{'datas': alldata} )
