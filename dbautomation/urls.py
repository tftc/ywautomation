#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.conf.urls import url
from dbautomation.views import login_view
from dbautomation.views import sqlupdate_view
from dbautomation.views import monitor_view
from dbautomation.views import serverconfig_view
from dbautomation.views import  dbgraphshow_view
from dbautomation.views import  mysqlreport_view
from dbautomation.views import  serverapply_view

urlpatterns = [
    # 用户登录登出和权限等基础配置
    url(r'^index/$', login_view.login, name='login'),
    url(r'^logout/$', login_view.logout, name='logout'),
    url(r'^dashboard/$', login_view.dashboard, name='dashboard'),

    # sql审核更新流程
    url('mysqldata/$', sqlupdate_view.mysqldata, name='mysqldata'),
    url('mysqlsqltask/$', sqlupdate_view.mysqlsqltask, name='mysqlsqltask'),
    url('mysqlsqlcontentinfo$', sqlupdate_view.mysqlsqlcontentinfo, name='mysqlsqlcontentinfo'),
    url('updatemysqlsqltask$', sqlupdate_view.updatemysqlsqltask, name='updatemysqlsqltask'),
    url('deletemysqltask$', sqlupdate_view.deletemysqltask, name='deletemysqltask'),
    url('mysqlcheckdata$', sqlupdate_view.mysqlcheckdata, name='mysqlcheckdata'),
    url('mysqlsqlexecute$', sqlupdate_view.mysqlsqlexecute, name='mysqlsqlexecute'),
    url('mysqlincepexecute$', sqlupdate_view.mysqlincepexecute, name='mysqlincepexecute'),
    url('mysqlfiletask/$', sqlupdate_view.mysqlfiletask, name='mysqlfiletask'),
    url('mysqlfinishtask/$', sqlupdate_view.mysqlfinishtask, name='mysqlfinishtask'),
    url('mysqlexecuteresult$', sqlupdate_view.mysqlexecuteresult, name='mysqlexecuteresult'),
    url('tobeexecutemysqltask/$', sqlupdate_view.tobeexecutemysqltask, name='tobeexecutemysqltask'),

    # server配置服务
    url('serverdatalist/$', serverconfig_view.serverdatalist, name='serverdatalist'),
    url('addserverdata/$', serverconfig_view.addserverdata, name='addserverdata'),
    url('updateserverdata$', serverconfig_view.updateserverdata, name='updateserverdata'),
    url('deleteserverdata$', serverconfig_view.deleteserverdata, name='deleteserverdata'),

    # mysql配置服务
    url('dbdatalist/$', serverconfig_view.dbdatalist, name='dbdatalist'),
    url('updatedbdata$', serverconfig_view.updatedbdata, name='updatedbdata'),
    url('adddbdata/$', serverconfig_view.adddbdata, name='adddbdata'),
    url('deletedbdata$', serverconfig_view.deletedbdata, name='deletedbdata'),

    # user用户配置
    url('userdatalist/$', serverconfig_view.userdatalist, name='userdatalist'),
    url('updateuserdata$', serverconfig_view.updateuserdata, name='updateuserdata'),
    url('adduserdata/$', serverconfig_view.adduserdata, name='adduserdata'),
    url('deleteuserdata$', serverconfig_view.deleteuserdata, name='deleteuserdata'),
    url('useuserdata$', serverconfig_view.useuserdata, name='useuserdata'),
    url('adduserpri$', serverconfig_view.adduserpri, name='adduserpri'),
    url('deleteuserpri$', serverconfig_view.deleteuserpri, name='deleteuserpri'),

    # port monitor data
    url('mysqlmonitor/$', monitor_view.mysqlmonitor, name='mysqlmonitor'),
    url('portmonitorlist/$', monitor_view.portmonitorlist, name='portmonitorlist'),
    url('addportmonitor/$', monitor_view.addportmonitor, name='addportmonitor'),
    url('updateportmonitor$', monitor_view.updateportmonitor, name='updateportmonitor'),
    url('deleteportmonitor$', monitor_view.deleteportmonitor, name='deleteportmonitor'),

    # db monitor data
    url('dbmonitorlist/$', monitor_view.dbmonitorlist, name='dbmonitorlist'),
    url('adddbmonitor/$', monitor_view.adddbmonitor, name='adddbmonitor'),
    url('updatedbmonitor$', monitor_view.updatedbmonitor, name='updatedbmonitor'),
    url('deletedbmonitor$', monitor_view.deletedbmonitor, name='deletedbmonitor'),
    url('dbmonitorrelationlist', monitor_view.dbmonitorrelationlist, name='dbmonitorrelationlist' ),
    url('adddbmonitorrelation', monitor_view.adddbmonitorrelation, name='adddbmonitorrelation' ),
    url('deletedbmonitorrealtion$', monitor_view.deletedbmonitorrealtion, name='deletedbmonitorrealtion' ),

    # os monitor data
    url('osmonitorlist/$', monitor_view.osmonitorlist, name='osmonitorlist'),
    url('addosmonitor/$', monitor_view.addosmonitor, name='addosmonitor'),
    url('updateosmonitor$', monitor_view.updateosmonitor, name='updateosmonitor'),
    url('deleteosmonitor$', monitor_view.deleteosmonitor, name='deleteosmonitor'),
    url('osmonitorrelationlist', monitor_view.osmonitorrelationlist, name='osmonitorrelationlist'),
    url('addosmonitorrelation', monitor_view.addosmonitorrelation, name='addosmonitorrelation'),
    url('deleteosmonitorrealtion', monitor_view.deleteosmonitorrealtion, name='deleteosmonitorrealtion'),

    #os 图形展示
    url('dbgraphshow/$', dbgraphshow_view.dbgraphshow, name='dbgraphshow'),
    url('dbminitorgraph$', dbgraphshow_view.dbminitorgraph, name='dbminitorgraph'),
    url('osminitorgraph$', dbgraphshow_view.osminitorgraph, name='osminitorgraph'),


    url('mysqlreportdata/$', mysqlreport_view.mysqlreportdata, name='mysqlreportdata' ),


    #server服务状态展示
    url('serverapplylist/$', serverapply_view.serverapplylist, name='serverapplylist'),
    url('addserverapply/$', serverapply_view.addserverapply, name='addserverapply'),
    url('showserverapply/$', serverapply_view.showserverapply, name='showserverapply' ),


    url('$',login_view.login, name='login'),
]
