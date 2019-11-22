import cx_Oracle as oracle
import subprocess

# conn = cx_Oracle.connect(TGS_WJ2 + '/' + TGS_WJ2 + '@' + '192.168.1.191' \
# + ' : ' + 1521 + '/'+ ORCL)
# cur = conn.cursor()
# sql = "select * from t_cms_info"
# cur.excute(sql)

# db = oracle.connect('jjzd/jjzd@192.168.31.54:1522/orcl')
# cursor = db.cursor()
# cursor.execute('select sysdate from dual')
# data = cursor.fetchone()
# print('Database time: %s' % data)
# cursor.close()
# db.close()


def pingCHK(ip):
    num = 1
    wait = 1000
    # 这种方式，终端不会显示运行结果
    ping = subprocess.Popen("ping -n {} -w {} {}".format(num, wait, ip), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exit_code = ping.wait()
    if exit_code != 0:
        return 1
    else:
        return 0


def updatedata(ip,zt):
    conn = oracle.connect('jjzd/jjzd@192.168.31.54:1522/orcl')
    cur = conn.cursor()
    sql = 'update t_device set zt = ' + zt + ' WHERE ip = ' + "'" + ip +"'"
    try:
       cur.execute(sql)
       conn.commit() 
       print("数据更新成功")
    except:
        conn.rollback()
        print("语句执行错误")
    conn.close()


db = oracle.connect('jjzd/jjzd@192.168.31.54:1522/orcl')
cursor = db.cursor()
cursor.execute('select ip,zt from t_device')
data = cursor.fetchall()
print(data)

for row in data:
    print(row[0])
    zt = str(pingCHK(row[0]))
    print(zt)
    updatedata(row[0], zt)
