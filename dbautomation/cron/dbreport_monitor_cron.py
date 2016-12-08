import commands
import datetime
import MySQLdb

selectsql="select a.db_id as db_id,db_name,db_port,db_user,db_allpri_pwd,defaults_db_name,server_name,outer_net,inner_net,use_outer_inner,func_name from db_data_info a join (select db_id from server_monitor_relation group by db_id) b on a.db_id=b.db_id join server_data_info c on a.server_id=c.server_id where db_type='mysql' order by db_id"
conn = MySQLdb.connect(host='hostname', user='user', passwd='pwd', db='db_name', port=3306, charset="utf8" )
cursor = conn.cursor( )
cursor.execute(selectsql)
result = cursor.fetchall( )
timedata =datetime.datetime.now()
ytime =timedata + datetime.timedelta(days=-1)
ytime = ytime.strftime("%Y-%m-%d")
tdtime = timedata.strftime("%Y-%m-%d")
for item in result:
    nDbid = item[0]
    nDbname = item[1]
    nDbport = item[2]
    nDbuser = item[3]
    nDbpwd = item[4]
    nDbdefaultdb = item[5]
    nFuncname = item[10]


    nNum1= '0'
    shelldata1="salt %s cmd.run 'mysqladmin -V'| sed '1d' | awk '{print $5}'" %(nFuncname)
    nNum1=commands.getoutput(shelldata1)


    nNum2 = '0'
    shelldata2 = "salt %s cmd.run 'mysqladmin -u%s -p%s -P%s status'| sed '1d'" % (nFuncname,nDbuser,nDbpwd,nDbport)
    nNum2 = commands.getoutput( shelldata2 )


    nNum3 = '0'
    shelldata3 = "salt %s cmd.run 'cat  /data/mysqlslowlog/day/slow_log_day_%s.log'| sed '1d'" % (nFuncname,ytime)
    nNum3 = commands.getoutput( shelldata3 )


    nNum4 = '0'
    shelldata4 = "salt %s cmd.run 'cat  /data/mysqlslowlog/week/slow_log_week__%s.log'| sed '1d'" % (nFuncname, ytime)
    nNum4 = commands.getoutput( shelldata3 )


    nNum5 = '0'
    shelldata5 = "salt %s cmd.run 'cat  /data/mysqlslowlog/month/slow_log_month_%s.log'| sed '1d'" % (nFuncname, ytime)
    nNum5 = commands.getoutput( shelldata3 )


    versionsql = "replace into server_report_monitor_result (db_id,version_values,mysql_status,1day_sql_slow,7day_sql_slow,30day_sql_slow,create_time) value (%s,%s,%s,%s,%s,%s,%s)"
    cursor = conn.cursor()
    cursor.execute(versionsql,[nDbid,nNum1,nNum2,nNum3,nNum4,nNum5,tdtime])
    conn.commit( )


