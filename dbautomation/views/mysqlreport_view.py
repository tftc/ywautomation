#!/usr/bin/env python
# -*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.db import connection
from dbautomation.model.mysqlreport_model import Mysqlreport
from dbautomation.model.dbgraphshow_model import Dbgraphshow
import datetime

# mysql数据库信息详情
def mysqlreportdata(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]

            Dbdatainfo = Mysqlreport.Dbdatainfo()
            nDbid=Dbdatainfo[0][0]
            nDbname = Dbdatainfo[0][1]

            ndays = 1
            nCreateTime = datetime.datetime.now().strftime('%Y-%m-%d')
            Report1 = Mysqlreport.Dbreportdata1(nDbid,nCreateTime,ndays)
            repotdata=[]
            for item in Report1:
                valuedata=item[3].replace(' # ','\r\n # ')
                repotdata.append(item[0])
                repotdata.append(nDbname)
                repotdata.append(item[1])
                repotdata.append(item[2])
                repotdata.append(valuedata)
                repotdata.append(ndays)
            print(repotdata)

            Report2 = Mysqlreport.Dbreportdaydata2(nDbid, nCreateTime,ndays)
            Report3 = Mysqlreport.Dbreportdaydata3(nDbid, nCreateTime, ndays)

            Report4 = Mysqlreport.Dbreportdayqps( nDbid, nCreateTime,ndays)
            Report4_repotdata = []
            Report4_monitor_values = []
            Report4_create_time = []

            for item in Report4:
                Report4_monitor_values.append(item[2])
                Report4_create_time.append(item[3])

            if Report4_monitor_values == []:
                Report4_repotdata.append( ['0'] )
            else:
                Report4_repotdata.append( Report4_monitor_values )
            if Report4_create_time == []:
                Report4_repotdata.append( ['0'] )
            else:
                Report4_repotdata.append(Report4_create_time)


            Report5 = Mysqlreport.Dbreportdaytps(nDbid, nCreateTime,ndays)
            Report5_repotdata = []
            Report5_monitor_values = []
            Report5_create_time = []

            for item in Report5:
                Report5_monitor_values.append( item[2] )
                if item[3] == '':
                    Report5_repotdata.append( ['0'] )
                else:
                    Report5_create_time.append( item[3])
            if Report5_monitor_values == []:
                Report5_repotdata.append( ['0'] )
            else:
                Report5_repotdata.append( Report5_monitor_values )
            if Report5_create_time == []:
                Report5_repotdata.append( ['0'] )
            else:
                Report5_repotdata.append(Report5_create_time)


            Report6 = Mysqlreport.Dbreportdayprocessnum( nDbid, nCreateTime,ndays)
            Report6_repotdata = []
            Report6_monitor_values1 = []
            Report6_monitor_values2 = []
            Report6_monitor_values3 = []
            Report6_create_time = []

            for item in Report6:
                Report6_monitor_values1.append( item[2] )
                Report6_monitor_values2.append( item[3] )
                Report6_monitor_values2.append( item[4] )
                Report6_create_time.append(item[5])
            if Report6_monitor_values1 == []:
                Report6_repotdata.append( ['0'] )
            else:
                Report6_repotdata.append(Report6_monitor_values1 )
            if Report6_monitor_values2 == []:
                Report6_repotdata.append( ['0'] )
            else:
                Report6_repotdata.append( Report6_monitor_values2 )
            if Report6_monitor_values3 == []:
                Report6_repotdata.append( ['0'] )
            else:
                Report6_repotdata.append( Report6_monitor_values3 )
            if Report6_create_time == []:
                Report6_repotdata.append( ['0'] )
            else:
                Report6_repotdata.append( Report6_create_time )


            Report7 = Mysqlreport.Dbreportdayreadbuffer( nDbid, nCreateTime,ndays)
            Report7_repotdata = []
            Report7_monitor_values = []
            Report7_create_time = []

            for item in Report7:
                Report7_monitor_values.append( item[2] )
                Report7_create_time.append( item[3])
            if Report7_monitor_values == []:
                Report7_repotdata.append( ['0'] )
            else:
                Report7_repotdata.append( Report7_monitor_values )
            if Report7_create_time == []:
                Report7_repotdata.append( ['0'] )
            else:
                Report7_repotdata.append( Report7_create_time )

            Report8 = Mysqlreport.Dbreportdaywritebuffer( nDbid, nCreateTime,ndays)
            Report8_repotdata = []
            Report8_monitor_values = []
            Report8_create_time = []

            for item in Report8:
                Report8_monitor_values.append( item[2] )
                Report8_create_time.append( item[3])
            if Report8_monitor_values == []:
                Report8_repotdata.append( ['0'] )
            else:
                Report8_repotdata.append( Report8_monitor_values )
            if Report8_create_time == []:
                Report8_repotdata.append( ['0'] )
            else:
                Report8_repotdata.append( Report8_create_time )

            Report9 = Mysqlreport.Dbreportdayinnodbbuffer( nDbid, nCreateTime,ndays)
            Report9_repotdata = []
            Report9_monitor_values = []
            Report9_create_time = []

            for item in Report9:
                Report9_monitor_values.append( item[2] )
                Report9_create_time.append( item[3])
            if Report9_monitor_values == []:
                Report9_repotdata.append( ['0'] )
            else:
                Report9_repotdata.append( Report9_monitor_values )
            if Report9_create_time == []:
                Report9_repotdata.append( ['0'] )
            else:
                Report9_repotdata.append( Report9_create_time )

            Report10 = Mysqlreport.Dbreportdayosload( nDbid, nCreateTime,ndays)
            Report10_repotdata = []
            Report10_monitor_values1 = []
            Report10_monitor_values2 = []
            Report10_monitor_values3 = []
            Report10_create_time = []

            for item in Report10:
                Report10_monitor_values1.append( item[0] )
                Report10_monitor_values2.append( item[1] )
                Report10_monitor_values3.append( item[2] )
                Report10_create_time.append( item[3])
            if Report10_monitor_values1 == []:
                Report10_repotdata.append( ['0'] )
            else:
                Report10_repotdata.append( Report10_monitor_values1 )
            if Report10_monitor_values2 == []:
                Report10_repotdata.append( ['0'] )
            else:
                Report10_repotdata.append( Report10_monitor_values2 )
            if Report10_monitor_values3 == []:
                Report10_repotdata.append( ['0'] )
            else:
                Report10_repotdata.append( Report10_monitor_values3 )
            if Report10_create_time == []:
                Report10_repotdata.append( ['0'] )
            else:
                Report10_repotdata.append( Report10_create_time )


            return render_to_response('mysqlreportdata.html',{'datas': Dbdatainfo,'num3': nUserrole,'num4': nCreateTime,'num5': ndays,'data1':repotdata,'data2':Report2,'data3':Report3,'data4':Report4_repotdata,'data5':Report5_repotdata,'data6':Report6_repotdata,'data7':Report7_repotdata,'data8':Report8_repotdata,'data9':Report9_repotdata,'data10':Report10_repotdata})
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        nDbid = req.POST.get('dbid')
        ndays = req.POST.get('timetype')
        nCreateTime = req.POST.get('datatime')
        print(nCreateTime)

        Dbdatainfo = Mysqlreport.Dbdatainfobyid( nDbid)
        nDbid = Dbdatainfo[0][0]
        nDbname = Dbdatainfo[0][1]

        Report1 = Mysqlreport.Dbreportdata1(nDbid,nCreateTime,ndays)
        repotdata = []
        for item in Report1:
            valuedata = item[3].replace( ' # ', '\r\n # ' )
            repotdata.append( item[0] )
            repotdata.append( nDbname )
            repotdata.append( item[1] )
            repotdata.append( item[2] )
            repotdata.append( valuedata )
            repotdata.append( ndays )


        Report2 = Mysqlreport.Dbreportdaydata2(nDbid, nCreateTime,ndays)
        Report3 = Mysqlreport.Dbreportdaydata3(nDbid, nCreateTime,ndays)

        Report4 = Mysqlreport.Dbreportdayqps(nDbid,nCreateTime,ndays)
        Report4_repotdata = []
        Report4_monitor_values = []
        Report4_create_time = []

        for item in Report4:
            Report4_monitor_values.append( item[2] )
            Report4_create_time.append( item[3])
        if Report4_monitor_values == []:
            Report4_repotdata.append( ['0'] )
        else:
            Report4_repotdata.append( Report4_monitor_values )
        if Report4_create_time == []:
            Report4_repotdata.append( ['0'] )
        else:
            Report4_repotdata.append( Report4_create_time )

        Report5 = Mysqlreport.Dbreportdaytps(nDbid,nCreateTime,ndays)
        Report5_repotdata = []
        Report5_monitor_values = []
        Report5_create_time = []

        for item in Report5:
            Report5_monitor_values.append( item[2] )
            Report5_create_time.append( item[3])
        if Report5_monitor_values == []:
            Report5_repotdata.append( ['0'] )
        else:
            Report5_repotdata.append( Report5_monitor_values )
        if Report5_create_time == []:
            Report5_repotdata.append( ['0'] )
        else:
            Report5_repotdata.append( Report5_create_time )

        Report6 = Mysqlreport.Dbreportdayprocessnum(nDbid,nCreateTime,ndays)
        Report6_repotdata = []
        Report6_monitor_values1 = []
        Report6_monitor_values2 = []
        Report6_monitor_values3 = []
        Report6_create_time = []

        for item in Report6:
            Report6_monitor_values1.append( item[2] )
            Report6_monitor_values2.append( item[3] )
            Report6_monitor_values2.append( item[4] )
            Report6_create_time.append( item[5])
        if Report6_monitor_values1 == []:
            Report6_repotdata.append( ['0'] )
        else:
            Report6_repotdata.append( Report6_monitor_values1 )
        if Report6_monitor_values2 == []:
            Report6_repotdata.append( ['0'] )
        else:
            Report6_repotdata.append( Report6_monitor_values2 )
        if Report6_monitor_values3 == []:
            Report6_repotdata.append( ['0'] )
        else:
            Report6_repotdata.append( Report6_monitor_values3 )
        if Report6_create_time == []:
            Report6_repotdata.append( ['0'] )
        else:
            Report6_repotdata.append( Report6_create_time )

        Report7 = Mysqlreport.Dbreportdayreadbuffer(nDbid,nCreateTime,ndays)
        Report7_repotdata = []
        Report7_monitor_values = []
        Report7_create_time = []

        for item in Report7:
            Report7_monitor_values.append( item[2] )
            Report7_create_time.append( item[3])
        if Report7_monitor_values == []:
            Report7_repotdata.append( ['0'] )
        else:
            Report7_repotdata.append( Report7_monitor_values )
        if Report7_create_time == []:
            Report7_repotdata.append( ['0'] )
        else:
            Report7_repotdata.append( Report7_create_time )

        Report8 = Mysqlreport.Dbreportdaywritebuffer(nDbid,nCreateTime,ndays)
        Report8_repotdata = []
        Report8_monitor_values = []
        Report8_create_time = []

        for item in Report8:
            Report8_monitor_values.append( item[2] )
            Report8_create_time.append( item[3] )
        if Report8_monitor_values == []:
            Report8_repotdata.append( ['0'] )
        else:
            Report8_repotdata.append( Report8_monitor_values )
        if Report8_create_time == []:
            Report8_repotdata.append( ['0'] )
        else:
            Report8_repotdata.append( Report8_create_time )

        Report9 = Mysqlreport.Dbreportdayinnodbbuffer(nDbid,nCreateTime,ndays)
        Report9_repotdata = []
        Report9_monitor_values = []
        Report9_create_time = []

        for item in Report9:
            Report9_monitor_values.append( item[2] )
            Report9_create_time.append( item[3])
        if Report9_monitor_values == []:
            Report9_repotdata.append( ['0'] )
        else:
            Report9_repotdata.append( Report9_monitor_values )
        if Report9_create_time == []:
            Report9_repotdata.append( ['0'] )
        else:
            Report9_repotdata.append( Report9_create_time )

        Report10 = Mysqlreport.Dbreportdayosload(nDbid,nCreateTime,ndays)
        Report10_repotdata = []
        Report10_monitor_values1 = []
        Report10_monitor_values2 = []
        Report10_monitor_values3 = []
        Report10_create_time = []

        for item in Report10:
            Report10_monitor_values1.append( item[0] )
            Report10_monitor_values2.append( item[1] )
            Report10_monitor_values3.append( item[2] )
            Report10_create_time.append( item[3])
        if Report10_monitor_values1 == []:
            Report10_repotdata.append( ['0'] )
        else:
            Report10_repotdata.append( Report10_monitor_values1 )
        if Report10_monitor_values2 == []:
            Report10_repotdata.append( ['0'] )
        else:
            Report10_repotdata.append( Report10_monitor_values2 )
        if Report10_monitor_values3 == []:
            Report10_repotdata.append( ['0'] )
        else:
            Report10_repotdata.append( Report10_monitor_values3 )
        if Report10_create_time == []:
            Report10_repotdata.append( ['0'] )
        else:
            Report10_repotdata.append( Report10_create_time )

        return render_to_response( 'mysqlreportdata.html',
                                   {'datas': Dbdatainfo, 'num3': nUserrole,'num4': nCreateTime,'num5': ndays,'data1': repotdata, 'data2': Report2,'data3': Report3, 'data4': Report4_repotdata, 'data5': Report5_repotdata,'data6': Report6_repotdata, 'data7': Report7_repotdata, 'data8': Report8_repotdata,'data9': Report9_repotdata, 'data10': Report10_repotdata} )
