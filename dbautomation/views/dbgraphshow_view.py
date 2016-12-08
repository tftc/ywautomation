#!/usr/bin/env python
# -*- coding: utf-8 -*-
# create by zhangsp 2016-06-06

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.db import connection
from dbautomation.model.sqlupdate_model import SqlUpdate
from dbautomation.model.dbgraphshow_model import Dbgraphshow
import datetime

# mysql数据库信息详情
def dbgraphshow(req):
    if not req.session.get( "sess_userid", False ):
        messagedata = '需要登录才可以访问'
        return HttpResponseRedirect( "/index/", {'message': messagedata} )
    else:
        nUserid = req.session["sess_userid"]
        nUserrole = req.session["sess_userrole"]
        dbinfolist=SqlUpdate.mysqlinfolist(nUserid)
        unfinishnum=SqlUpdate.mysqlunfinishtasknum(nUserid,nUserrole)
        finishnum = SqlUpdate.mysqlfinishtasknum(nUserid,nUserrole)

        return render_to_response('dbgraphshow.html', {'datas': dbinfolist,'num1': unfinishnum,'num2': finishnum,'num3': nUserrole})


def dbminitorgraph(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            nDbid = req.GET['dbid']
            endtime1 = datetime.datetime.now( ).strftime( "%Y-%m-%d %H:%M:%S" )
            starttime = datetime.datetime.now( ) + datetime.timedelta( days=-1 )
            starttime1 = starttime.strftime( "%Y-%m-%d %H:%M:%S" )
            nMysqlqps = Dbgraphshow.mysqlqpsdata(nDbid,starttime1,endtime1)
            print(nMysqlqps);
            exit;
            qpsdate = []
            qpsvalue = []
            alldata =[]
            for item in nMysqlqps:
                qpsdate.append(item[0])
                qpsvalue.append(item[1])
            if qpsdate == []:
                alldata.append(['0'])
            else:
                alldata.append(qpsdate)
            if qpsvalue == []:
                alldata.append(['0'])
            else:
                alldata.append(qpsvalue)

            ## mysql  增删改查
            nMysqlidus = Dbgraphshow.mysqlidusdata( nDbid, starttime1, endtime1 )
            idusdate=[]
            insertvalue = []
            deletevalue = []
            updatevalue = []
            selectvalue = []
            allidusdata = []
            for item in nMysqlidus:
                idusdate.append( item[0])
                insertvalue.append(item[1])
                deletevalue.append(item[2])
                updatevalue.append(item[3])
                selectvalue.append(item[4])
            if idusdate == []:
                allidusdata.append(['0'])
            else:
                allidusdata.append(idusdate)
            if insertvalue == []:
                allidusdata.append(['0'])
            else:
                allidusdata.append(insertvalue)
            if deletevalue == []:
                allidusdata.append(['0'])
            else:
                allidusdata.append(deletevalue)
            if updatevalue == []:
                allidusdata.append(['0'])
            else:
                allidusdata.append(updatevalue)
            if selectvalue == []:
                allidusdata.append(['0'])
            else:
                allidusdata.append(selectvalue)

            ## mysql processlist  数量
            nMysqlprocesslistnum = Dbgraphshow.mysqlprocesslistnum( nDbid, starttime1, endtime1 )
            processlistdate = []
            processlistvalue = []
            allprocesslistdata = []
            for item in nMysqlprocesslistnum:
                processlistdate.append( item[0])
                processlistvalue.append( item[1] )

            if processlistdate == []:
                allprocesslistdata.append( ['0'] )
            else:
                allprocesslistdata.append( processlistdate )
            if processlistvalue == []:
                allprocesslistdata.append( ['0'] )
            else:
                allprocesslistdata.append( processlistvalue )

            ## mysql 临时表使用
            nMysqlnumtmptable = Dbgraphshow.mysqlnumtmptable( nDbid, starttime1, endtime1 )
            tmptabledate = []
            tmptablevalue = []
            alltmptabledata = []
            for item in nMysqlnumtmptable:
                tmptabledate.append( item[0])
                tmptablevalue.append( item[1] )
            if tmptabledate == []:
                alltmptabledata.append( ['0'] )
            else:
                alltmptabledata.append(tmptabledate)
            if tmptablevalue == []:
                alltmptabledata.append( ['0'] )
            else:
                alltmptabledata.append(tmptablevalue)

            ## mysql 索引read命中率
            nMysqlkeybufferreadhits = Dbgraphshow.mysqlkeybufferreadhits( nDbid, starttime1, endtime1 )
            bufferreadhitsdate = []
            bufferreadhitsvalue = []
            allbufferreadhitsdata = []

            for item in nMysqlkeybufferreadhits:
                bufferreadhitsdate.append( item[0] )
                bufferreadhitsvalue.append( item[1] )
            if bufferreadhitsdate == []:
                allbufferreadhitsdata.append( ['0'] )
            else:
                allbufferreadhitsdata.append(bufferreadhitsdate)
            if bufferreadhitsvalue == []:
                allbufferreadhitsdata.append( ['0'] )
            else:
                allbufferreadhitsdata.append(bufferreadhitsvalue)

            ## mysql 索引write命中率
            nMysqlkeybufferwritehits = Dbgraphshow.mysqlkeybufferwritehits( nDbid, starttime1, endtime1 )
            keybufferwritehitsledate = []
            keybufferwritehitsvalue = []
            allkeybufferwritehitsdata = []

            for item in nMysqlkeybufferwritehits:
                keybufferwritehitsledate.append(item[0])
                keybufferwritehitsvalue.append(item[1])

            if keybufferwritehitsledate == []:
                allkeybufferwritehitsdata.append( ['0'] )
            else:
                allkeybufferwritehitsdata.append(keybufferwritehitsledate)
            if keybufferwritehitsvalue == []:
                allkeybufferwritehitsdata.append( ['0'] )
            else:
                allkeybufferwritehitsdata.append(keybufferwritehitsvalue)

            ## INNNODB buffer命中率
            nMysqlinnodbbufferreadhits = Dbgraphshow.mysqlinnodbbufferreadhits( nDbid, starttime1, endtime1 )
            innodbbufferreadhitsdate = []
            innodbbufferreadhitsvalue = []
            allinnodbbufferreadhitsdata = []

            for item in nMysqlinnodbbufferreadhits:
                innodbbufferreadhitsdate.append(item[0].strftime( "%Y-%m-%d %H:%M:%S" ))
                innodbbufferreadhitsvalue.append(item[1])

            if innodbbufferreadhitsdate == []:
                allinnodbbufferreadhitsdata.append(['0'])
            else:
                allinnodbbufferreadhitsdata.append( innodbbufferreadhitsdate )
            if innodbbufferreadhitsvalue == []:
                allinnodbbufferreadhitsdata.append(['0'])
            else:
                allinnodbbufferreadhitsdata.append( innodbbufferreadhitsvalue )

            endtime = datetime.datetime.now( ).strftime( "%Y-%m-%d %H:%M:%S" )
            starttime = datetime.datetime.now( ) + datetime.timedelta( days=-1 )
            starttime = starttime.strftime( "%Y-%m-%d %H:%M:%S" )
            return render_to_response('dbmonitorgraph.html', {'datas': alldata,'datas1': allidusdata,'datas2': allprocesslistdata,'datas3': alltmptabledata,'datas4': allbufferreadhitsdata,'datas5': allkeybufferwritehitsdata,'datas6': allinnodbbufferreadhitsdata,'num3': nUserrole,'num5': starttime,'num6': endtime,'num7':nDbid})
    elif req.method == 'POST':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            nDbid = req.POST['dbid']
            starttime1 = req.POST['begintime']
            endtime1 = req.POST['endtime']
            nMysqlqps = Dbgraphshow.mysqlqpsdata( nDbid, starttime1, endtime1 )

            qpsdate = []
            qpsvalue = []
            alldata = []
            for item in nMysqlqps:
                qpsdate.append( item[0] )
                qpsvalue.append( item[1] )
            if qpsdate == []:
                alldata.append( ['0'] )
            else:
                alldata.append( qpsdate )
            if qpsvalue == []:
                alldata.append( ['0'] )
            else:
                alldata.append( qpsvalue )

            ## mysql  增删改查
            nMysqlidus = Dbgraphshow.mysqlidusdata( nDbid, starttime1, endtime1 )
            idusdate = []
            insertvalue = []
            deletevalue = []
            updatevalue = []
            selectvalue = []
            allidusdata = []
            for item in nMysqlidus:
                idusdate.append( item[0] )
                insertvalue.append( item[1] )
                deletevalue.append( item[2] )
                updatevalue.append( item[3] )
                selectvalue.append( item[4] )
            if idusdate == []:
                allidusdata.append( ['0'] )
            else:
                allidusdata.append( idusdate )
            if insertvalue == []:
                allidusdata.append( ['0'] )
            else:
                allidusdata.append( insertvalue )
            if deletevalue == []:
                allidusdata.append( ['0'] )
            else:
                allidusdata.append( deletevalue )
            if updatevalue == []:
                allidusdata.append( ['0'] )
            else:
                allidusdata.append( updatevalue )
            if selectvalue == []:
                allidusdata.append( ['0'] )
            else:
                allidusdata.append( selectvalue )

            ## mysql processlist  数量
            nMysqlprocesslistnum = Dbgraphshow.mysqlprocesslistnum( nDbid, starttime1, endtime1 )
            processlistdate = []
            processlistvalue = []
            allprocesslistdata = []
            for item in nMysqlprocesslistnum:
                processlistdate.append( item[0] )
                processlistvalue.append( item[1] )

            if processlistdate == []:
                allprocesslistdata.append( ['0'] )
            else:
                allprocesslistdata.append( processlistdate )
            if processlistvalue == []:
                allprocesslistdata.append( ['0'] )
            else:
                allprocesslistdata.append( processlistvalue )

            ## mysql 临时表使用
            nMysqlnumtmptable = Dbgraphshow.mysqlnumtmptable( nDbid, starttime1, endtime1 )
            tmptabledate = []
            tmptablevalue = []
            alltmptabledata = []
            for item in nMysqlnumtmptable:
                tmptabledate.append( item[0] )
                tmptablevalue.append( item[1] )
            if tmptabledate == []:
                alltmptabledata.append( ['0'] )
            else:
                alltmptabledata.append( tmptabledate )
            if tmptablevalue == []:
                alltmptabledata.append( ['0'] )
            else:
                alltmptabledata.append( tmptablevalue )

            ## mysql 索引read命中率
            nMysqlkeybufferreadhits = Dbgraphshow.mysqlkeybufferreadhits( nDbid, starttime1, endtime1 )
            bufferreadhitsdate = []
            bufferreadhitsvalue = []
            allbufferreadhitsdata = []

            for item in nMysqlkeybufferreadhits:
                bufferreadhitsdate.append( item[0] )
                bufferreadhitsvalue.append( item[1] )
            if bufferreadhitsdate == []:
                allbufferreadhitsdata.append( ['0'] )
            else:
                allbufferreadhitsdata.append( bufferreadhitsdate )
            if bufferreadhitsvalue == []:
                allbufferreadhitsdata.append( ['0'] )
            else:
                allbufferreadhitsdata.append( bufferreadhitsvalue )

            ## mysql 索引write命中率
            nMysqlkeybufferwritehits = Dbgraphshow.mysqlkeybufferwritehits( nDbid, starttime1, endtime1 )
            keybufferwritehitsledate = []
            keybufferwritehitsvalue = []
            allkeybufferwritehitsdata = []

            for item in nMysqlkeybufferwritehits:
                keybufferwritehitsledate.append( item[0] )
                keybufferwritehitsvalue.append( item[1] )

            if keybufferwritehitsledate == []:
                allkeybufferwritehitsdata.append( ['0'] )
            else:
                allkeybufferwritehitsdata.append( keybufferwritehitsledate )
            if keybufferwritehitsvalue == []:
                allkeybufferwritehitsdata.append( ['0'] )
            else:
                allkeybufferwritehitsdata.append( keybufferwritehitsvalue )

            ## INNNODB buffer命中率
            nMysqlinnodbbufferreadhits = Dbgraphshow.mysqlinnodbbufferreadhits( nDbid, starttime1, endtime1 )
            innodbbufferreadhitsdate = []
            innodbbufferreadhitsvalue = []
            allinnodbbufferreadhitsdata = []

            for item in nMysqlinnodbbufferreadhits:
                innodbbufferreadhitsdate.append( item[0].strftime( "%Y-%m-%d %H:%M:%S" ) )
                innodbbufferreadhitsvalue.append( item[1] )

            if innodbbufferreadhitsdate == []:
                allinnodbbufferreadhitsdata.append( ['0'] )
            else:
                allinnodbbufferreadhitsdata.append( innodbbufferreadhitsdate )
            if innodbbufferreadhitsvalue == []:
                allinnodbbufferreadhitsdata.append( ['0'] )
            else:
                allinnodbbufferreadhitsdata.append( innodbbufferreadhitsvalue )

            return render_to_response( 'dbmonitorgraph.html',
                                        {'datas': alldata, 'datas1': allidusdata, 'datas2': allprocesslistdata,
                                        'datas3': alltmptabledata, 'datas4': allbufferreadhitsdata,
                                        'datas5': allkeybufferwritehitsdata, 'datas6': allinnodbbufferreadhitsdata,
                                        'num3': nUserrole, 'num5': starttime1, 'num6': endtime1, 'num7': nDbid} )


def osminitorgraph(req):
    if req.method == 'GET':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            nServerid = req.GET['serverid']
            endtime1 = datetime.datetime.now( ).strftime( "%Y-%m-%d %H:%M:%S" )
            starttime = datetime.datetime.now( ) + datetime.timedelta( days=-1 )
            starttime1 = starttime.strftime( "%Y-%m-%d %H:%M:%S" )

            nOsiouserd = Dbgraphshow.osiouserd( nServerid, starttime1, endtime1 )
            iouserddate = []
            iouserdvalue = []
            alliouserddata = []
            for item in nOsiouserd:
                iouserddate.append( item[0].strftime( "%Y-%m-%d %H:%M:%S" ) )
                iouserdvalue.append( item[1] )
            if iouserddate == []:
                alliouserddata.append( ['0'] )
            else:
                alliouserddata.append( iouserddate )
            if iouserdvalue == []:
                alliouserddata.append( ['0'] )
            else:
                alliouserddata.append( iouserdvalue )



            nOfreecpu = Dbgraphshow.osfreecpu( nServerid, starttime1, endtime1 )
            freecpudate = []
            freecpuvalue = []
            allfreecpudata = []
            for item in nOfreecpu:
                freecpudate.append( item[0].strftime( "%Y-%m-%d %H:%M:%S" ) )
                freecpuvalue.append( item[1] )
            if freecpudate == []:
                allfreecpudata.append( ['0'] )
            else:
                allfreecpudata.append( freecpudate )
            if freecpuvalue == []:
                allfreecpudata.append( ['0'] )
            else:
                allfreecpudata.append( freecpuvalue )



            nOsload = Dbgraphshow.osload( nServerid, starttime1, endtime1 )
            osloaddate = []
            osload1value = []
            osload5value = []
            osload15value = []
            allosloaddata = []
            for item in nOsload:
                osloaddate.append( item[0].strftime( "%Y-%m-%d %H:%M:%S" ) )
                osload1value.append( item[1] )
                osload5value.append( item[2] )
                osload15value.append( item[3] )
            if osloaddate == []:
                allosloaddata.append( ['0'] )
            else:
                allosloaddata.append( osloaddate )
            if osload1value == []:
                allosloaddata.append( ['0'] )
            else:
                allosloaddata.append( osload1value )
            if osload5value == []:
                allosloaddata.append( ['0'] )
            else:
                allosloaddata.append( osload5value )
            if osload15value == []:
                allosloaddata.append( ['0'] )
            else:
                allosloaddata.append( osload15value )

            endtime = datetime.datetime.now( ).strftime( "%Y年%m月%d日 %H:%M:%S" )
            starttime = datetime.datetime.now( ) + datetime.timedelta( days=-1 )
            starttime = starttime.strftime( "%Y年%m月%d日 %H:%M:%S" )
            return render_to_response('osmonitorgraph.html', {'datas': alliouserddata,'datas1': allfreecpudata,'datas2': allosloaddata,'num3': nUserrole,'num5': starttime,'num6': endtime, 'num7': nServerid})
    if req.method == 'POST':
        if not req.session.get( "sess_userid", False ):
            messagedata = '需要登录才可以访问'
            return HttpResponseRedirect( "/index/", {'message': messagedata} )
        else:
            nUserid = req.session["sess_userid"]
            nUserrole = req.session["sess_userrole"]
            nServerid = req.POST['serverid']
            starttime1 = req.POST['begintime']
            endtime1 = req.POST['endtime']

            nOsiouserd = Dbgraphshow.osiouserd( nServerid, starttime1, endtime1 )
            iouserddate = []
            iouserdvalue = []
            alliouserddata = []
            for item in nOsiouserd:
                iouserddate.append( item[0].strftime( "%Y-%m-%d %H:%M:%S" ) )
                iouserdvalue.append( item[1] )
            if iouserddate == []:
                alliouserddata.append( ['0'] )
            else:
                alliouserddata.append( iouserddate )
            if iouserdvalue == []:
                alliouserddata.append( ['0'] )
            else:
                alliouserddata.append( iouserdvalue )

            nOfreecpu = Dbgraphshow.osfreecpu( nServerid, starttime1, endtime1 )
            freecpudate = []
            freecpuvalue = []
            allfreecpudata = []
            for item in nOfreecpu:
                freecpudate.append( item[0].strftime( "%Y-%m-%d %H:%M:%S" ) )
                freecpuvalue.append( item[1] )
            if freecpudate == []:
                allfreecpudata.append( ['0'] )
            else:
                allfreecpudata.append( freecpudate )
            if freecpuvalue == []:
                allfreecpudata.append( ['0'] )
            else:
                allfreecpudata.append( freecpuvalue )

            nOsload = Dbgraphshow.osload( nServerid, starttime1, endtime1 )
            osloaddate = []
            osload1value = []
            osload5value = []
            osload15value = []
            allosloaddata = []
            for item in nOsload:
                osloaddate.append( item[0].strftime( "%Y-%m-%d %H:%M:%S" ) )
                osload1value.append( item[1] )
                osload5value.append( item[2] )
                osload15value.append( item[3] )
            if osloaddate == []:
                allosloaddata.append( ['0'] )
            else:
                allosloaddata.append( osloaddate )
            if osload1value == []:
                allosloaddata.append( ['0'] )
            else:
                allosloaddata.append( osload1value )
            if osload5value == []:
                allosloaddata.append( ['0'] )
            else:
                allosloaddata.append( osload5value )
            if osload15value == []:
                allosloaddata.append( ['0'] )
            else:
                allosloaddata.append( osload15value )

            endtime = datetime.datetime.now( ).strftime( "%Y年%m月%d日 %H:%M:%S" )
            starttime = datetime.datetime.now( ) + datetime.timedelta( days=-1 )
            starttime = starttime.strftime( "%Y年%m月%d日 %H:%M:%S" )
            return render_to_response( 'osmonitorgraph.html',
                                       {'datas': alliouserddata, 'datas1': allfreecpudata, 'datas2': allosloaddata,
                                        'num3': nUserrole, 'num5': starttime, 'num6': endtime, 'num7': nServerid} )


