import re
# 处理视图字符串，增强可读性
def viewFormat(view):
    selectIndex = view.lower().index('select')
    fromIndex = view.lower().index('from')
    selectSql = view[selectIndex + 6:fromIndex].replace('`','')
    # sql = re.search('AS [.*\,]*', selectSql).group()
    # sql = re.sub('AS', '', selectSql)
    print(selectSql)


if __name__ == '__main__':
    view = """
    CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `User_Base_V` AS select `c`.`id` AS `id`,`c`.`ub_username` AS `ub_username`,`c`.`ub_realname` AS `ub_realname`,`c`.`ub_password` AS `ub_password`,`c`.`ub_wxno` AS `ub_wxno`,`c`.`ub_type` AS `ub_type`,`c`.`ub_acctype` AS `ub_acctype`,`c`.`ub_departmentid` AS `ub_departmentid`,`c`.`ub_rlcompanyid` AS `ub_rlcompanyid`,`c`.`ub_telephone` AS `ub_telephone`,`c`.`adid` AS `adid`,`c`.`ub_isinvalid` AS `ub_isinvalid`,`c`.`adid` AS `ownercompanyid`,`c`.`ub_username` AS `user_name`,`a`.`rar_roleid` AS `user_roleid`,`e`.`adr_name` AS `user_rolename`,`a`.`rar_itemid` AS `user_authitemid`,`b`.`sa_name` AS `user_authitemname` from ((((`User_Base` `c` left join `UR_Relation` `d` on((`d`.`urr_userid` = `c`.`id`))) left join `RA_Relation` `a` on((`a`.`rar_roleid` = `d`.`urr_roleid`))) left join `Sys_AuthItem` `b` on((`a`.`rar_itemid` = `b`.`id`))) left join `AD_Role` `e` on((`e`.`id` = `d`.`urr_roleid`))) where (`c`.`ub_isinvalid` = 0)
    """
    viewFormat(view)



