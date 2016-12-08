import commands
import datetime
import MySQLdb
import top.api

req=top.api.AlibabaAliqinFcSmsNumSendRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.extend="123456"
req.sms_type="normal"
req.sms_free_sign_name="阿里大鱼"
req.sms_param="{\"code\":\"1234\",\"product\":\"alidayu\"}"
req.rec_num="13000000000"
req.sms_template_code="SMS_585014"
try:
    resp= req.getResponse()
    print(resp)
except Exception,e:
    print(e)



selectsql='select a.monitor_id,server_name,outer_net,inner_net,use_outer_inner,monitor_target_value from server_monitor_port_data a join server_monitor_prototype b on a.monitor_id=b.monitor_id join server_data_info c on b.server_id=c.server_id where error_times>0 and report_times<=3'

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
    nDbid = item[7]
    nDbport = item[8]
    nDbuser = item[9]
    nDballpripwd = item[10]


    if nUseouterinner == 1:
        nHostname = nInnernet
    elif nUseouterinner == 2:
        nHostname = nOuternet

    shelldata='mysql -u%s -p%s -h%s -P%s -N -e "%s"' % (nDbuser,nDballpripwd,nHostname,nDbport,nMonitorshell)
    nNum=commands.getoutput(shelldata)

    resultsql = "insert into server_monitor_result (monitor_id,server_id,db_id,monitor_values,create_time) value (%d,%d,%d,'%s','%s')" %(nMonitorid,nServerid,nDbid,nNum,timedata)
    cursor = conn.cursor()
    cursor.execute(resultsql)
    conn.commit( )


