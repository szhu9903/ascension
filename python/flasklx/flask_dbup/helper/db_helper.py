from resource import db_url,session,engine

connection = engine.connect()

def getSelect(sql,pargm=None):
    if not pargm:
        sql = sql.replace('%','%%')
    try:
        res = connection.execute(sql,pargm) if pargm else connection.execute(sql)
    except Exception as er:
        print(er)
        return None
    # connection.close()
    return res.fetchall()

def updateSql(sql,pargm=None):
    connection = engine.connect()
    if not pargm:
        sql = sql.replace('%','%%')
    res = connection.execute(sql, pargm) if pargm else connection.execute(sql)
    try:
        return res.fetchone()
    except:
        return res.rowcount



