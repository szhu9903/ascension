from resource import db_url,session


def getSelect(sql,pargm=None):
    if not pargm:
        sql = sql.replace('%','%%')
    try:
        res = session.execute(sql,pargm) if pargm else session.execute(sql)
    except Exception as er:
        print(er)
        return None
    return res.fetchall()

def updateSql(sql,pargm=None):
    if not pargm:
        sql = sql.replace('%','%%')
    res = session.execute(sql, pargm) if pargm else session.execute(sql)
    try:
        return res.fetchone()
    except:
        return res.rowcount



