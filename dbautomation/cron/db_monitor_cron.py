import commands
import datetime
import MySQLdb

selectsql="select a.monitor_id as monitor_id,b.server_id as server_id,outer_net,inner_net,use_outer_inner,monitor_target_name,monitor_shell,b.db_id as db_id,db_port,db_user,db_allpri_pwd  from server_monitor_prototype a join server_monitor_relation b on a.monitor_id=b.monitor_id join db_data_info c on b.db_id=c.db_id join server_data_info d on b.server_id=d.server_id where monitor_type in (1,2) and is_monitor=1"

conn = MySQLdb.connect(host='hostname', user='user', passwd='pwd', db='db_name', port=3306, charset="utf8" )
cursor = conn.cursor( )
cursor.execute(selectsql)
result = cursor.fetchall()
timedata = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
timedata=timedata+':00'
for item in result:
    nMonitorid = item[0]
    nServerid = item[1]
    nOuternet = item[2]
    nInnernet = item[3]
    nUseouterinner = item[4]
    nMonitortargetname = item[5]
    nMonitorshell = item[6]
    nDbid = item[7]
    nDbport = item[8]
    nDbuser = item[9]
    nDballpripwd = item[10]


    if nUseouterinner == 1:
        nHostname = nInnernet
    elif nUseouterinner == 2:
        nHostname = nOuternet

    nNum = 0
    shelldata='mysql -u%s -p%s -h%s -P%s -N -e "%s"' % (nDbuser,nDballpripwd,nHostname,nDbport,nMonitorshell)
    nNum=commands.getoutput(shelldata)

    resultsql = "replace into server_monitor_result (monitor_id,server_id,db_id,monitor_values,create_time) value (%d,%d,%d,'%s','%s')" %(nMonitorid,nServerid,nDbid,nNum,timedata)
    cursor = conn.cursor()
    cursor.execute(resultsql)
    conn.commit()

    updatesql = "update server_monitor_result a,server_monitor_result b set a.real_values=round(a.monitor_values-b.monitor_values,4) where a.monitor_id=b.monitor_id and a.db_id=b.db_id and (unix_timestamp(a.create_time)-120)=unix_timestamp(b.create_time) and a.db_id=%s and a.monitor_id=%s and a.create_time='%s'" % (nDbid, nMonitorid, timedata)
    cursor = conn.cursor( )
    cursor.execute(updatesql)
    conn.commit( )



