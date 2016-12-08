#!/usr/bin/env python
#-*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from dbautomation.model.login_model import Login


def login(req):
    if req.method == 'GET':
        return render_to_response('index.html',context_instance=RequestContext(req))
    else:
        nUsername = req.POST.get('username')
        nPasswd = req.POST.get('password')
        AccountNum=Login.checklogindata(nUsername,nPasswd)
        print AccountNum
        if AccountNum == 1:
            AccountData = Login.usersessiondata(nUsername, nPasswd)
            if AccountData[2] == 1:
                req.session["sess_userid"] = AccountData[0]
                req.session["sess_username"] = nUsername
                req.session["sess_userrole"] = AccountData[1]
                return HttpResponseRedirect( "/dashboard/" )
            else:
                messagedata=[]
                messagedata.append( 'this account is forbiden,plaese get message from administor')
                return HttpResponseRedirect("index.html", {'message':messagedata} )
        else:
            messagedata = []
            messagedata.append( 'user or passwd is error' )
            return HttpResponseRedirect("/index/",{'message':messagedata})

def logout(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message':messagedata} )
    else:
        del req.session["sess_userid"]
        del req.session["sess_username"]
        del req.session["sess_userrole"]
        return HttpResponseRedirect("/index/")

def dashboard(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        UserRole = req.session["sess_userrole"]
        print UserRole
        return render_to_response('dashboard.html',{'datas': UserRole} )
