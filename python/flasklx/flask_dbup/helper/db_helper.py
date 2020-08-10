from resource import db_url,mysql_db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(mysql_db_url)


def getSelect(sql,pargm=None):
    if not pargm:
        sql = sql.replace('%','%%')
    try:
        res = engine.execute(sql,pargm) if pargm else engine.execute(sql)
    except Exception as er:
        print(er)
        return None
    return res.fetchall()

def updateSql(sql,pargm=None):
    if not pargm:
        sql = sql.replace('%','%%')
    res = engine.execute(sql, pargm) if pargm else engine.execute(sql)
    try:
        return res.fetchone()
    except:
        return res.rowcount



