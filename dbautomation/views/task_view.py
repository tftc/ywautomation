from dbautomation.cron.portmonitor_cron import add

def addtest(req):
    add.delay( 2, 2 )