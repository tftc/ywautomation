import commands
import datetime
import MySQLdb

selectsql='select a.monitor_id as monitor_id,b.server_id as server_id,outer_net,inner_net,use_outer_inner,monitor_target_name,monitor_shell,func_name from server_monitor_prototype a join server_monitor_relation b on a.monitor_id=b.monitor_id join server_data_info c on b.server_id=c.server_id where monitor_type=3 and is_monitor=1'

conn = MySQLdb.connect(host='hostname', user='user', passwd='pwd', db='db_name', port=3306, charset="utf8" )
cursor = conn.cursor( )
cursor.execute(selectsql)
result = cursor.fetchall( )
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
    nFuncname = item[7]


    if nUseouterinner == 1:
        nHostname = nInnernet
    elif nUseouterinner == 2:
        nHostname = nOuternet
    nNum=0
    shelldata='salt %s cmd.run "%s"|tail -1|awk \'{print $1}\'' % (nFuncname,nMonitorshell)
    nNum=commands.getoutput(shelldata)

    resultsql = "replace into server_monitor_result (monitor_id,server_id,monitor_values,create_time) value (%d,%d,'%s','%s')" %(nMonitorid,nServerid,nNum,timedata)
    cursor = conn.cursor()
    cursor.execute(resultsql)
    conn.commit( )


