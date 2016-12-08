import commands

import MySQLdb

selectsql='select a.monitor_id as monitor_id,b.server_id as server_id,outer_net,inner_net,use_outer_inner,monitor_target_name,monitor_target_value from server_monitor_prototype a join server_monitor_relation b on a.monitor_id=b.monitor_id join server_data_info c on b.server_id=c.server_id  where monitor_type=4 and is_monitor=1'

conn = MySQLdb.connect(host='hostname', user='user', passwd='pwd', db='db_name', port=3306, charset="utf8" )
cursor = conn.cursor( )
cursor.execute(selectsql)
result = cursor.fetchall( )
for item in result:
    nMonitorid = item[0]
    nServerid = item[1]
    nOuternet = item[2]
    nInnernet = item[3]
    nUseouterinner = item[4]
    nMonitortargetname = item[5]
    nMonitortargetvalue = item[6]

    if nUseouterinner == 1:
        nHostname = nInnernet
    elif nUseouterinner == 2:
        nHostname = nOuternet

    shelldata='nmap -p %s  %s |grep open|wc -l' %(nMonitortargetvalue,nHostname)
    nNum=commands.getoutput(shelldata)
    nNum=nNum.strip()

    if nNum == '0':
        updatesql = 'replace into server_monitor_port_data (monitor_id,server_id,server_port) values (%s,%s,%s) ON DUPLICATE KEY UPDATE error_times=error_times+1'
        cursor = conn.cursor( )
        cursor.execute(updatesql,[nMonitorid,nServerid,nMonitortargetvalue])
        cursor.close( )
        conn.commit( )
        conn.close( )
    elif nNum == '1':
        updatesql = 'replace into server_monitor_port_data (monitor_id,server_id,server_port) values (%s,%s,%s)'
        cursor = conn.cursor( )
        cursor.execute(updatesql,[nMonitorid,nServerid,nMonitortargetvalue])
        cursor.close( )
        conn.commit( )
        conn.close( )


