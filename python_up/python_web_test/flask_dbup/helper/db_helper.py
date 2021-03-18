from resource import db_url,session,engine,connection



def getSelect(sql,pargm=None,tran=None):

    if not pargm:
        sql = sql.replace('%','%%')
    try:
        res = connection.execute(sql,pargm) if pargm else connection.execute(sql)
    except Exception as er:
        print(er)
        return None
    return res.fetchall()

def updateSql(sql,pargm=None,tran=None):
    # if isinstance(sql,list):
    #     try:
    #         for sqli in sql:
    #             connection.execute(sqli)
    #         tran.commit()
    #         return True
    #     except Exception as er:
    #         print(er)
    #         tran.rollback()
    #         return False
    # else:


    if not pargm:
        sql = sql.replace('%','%%')
    res = connection.execute(sql, pargm) if pargm else connection.execute(sql)
    try:
        return res.fetchone()
    except:
        return res.rowcount



