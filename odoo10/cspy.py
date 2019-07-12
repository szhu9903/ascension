
from odoo import models, fields, api
import datetime
import calendar
from dateutil.relativedelta import relativedelta
from helper.choose_help import getbbbh
import pytz
from odoo.exceptions import UserError, AccessError
from helper.permit_helper import check_permit

class yszlb(models.Model):
    _name = 'yszlb'
    _description = u'应收账龄表'
    _inherit = ['mail.thread']
    _rec_name = "bbbh"
    _order = 'create_date desc'

    bbbh = fields.Char('编号', track_visibility='onchange')
    bbmc = fields.Char('报表名称', track_visibility='onchange')
    cjr = fields.Many2one('code', '创建人')
    bbrq = fields.Datetime("创建时间", track_visibility='onchange')


    jsr = fields.Many2one('code', '接收人')
    jsrq = fields.Datetime("接收时间", track_visibility='onchange')
    zt = fields.Char('状态', track_visibility='onchange')
    bbqjn = fields.Char('报表期间年', track_visibility='onchange')
    bbqjy = fields.Char('报表期间月', track_visibility='onchange')
    gsmc = fields.Many2one('gs', '归属公司')

    display_bbqj = fields.Char('报表期间', track_visibility='onchange')
    display_gsqj = fields.Char('归属公司报表期间', track_visibility='onchange')

    @api.model
    def create(self,vals):
        #判断是否有录入权限
        if not check_permit(self,'yszlb','录入'):
            gsdmc = self.env.user.glyh.dqgs.name
            gsmc = gsdmc.encode('utf-8')
            yhdmc = self.env.user.glyh.name
            yhmc = yhdmc.encode('utf-8')
            raise UserError('当前公司为:%s,用户:%s,没有录入权限'%(gsmc,yhmc))
        login_user = self.env.user
        #期间
        select_xzqj_sql = \
            """
            select s2.bbqjin,s2.bbqjy from xzqj s1 
            left join bbqj s2 on s1.qyqj = s2.id
            """
        self._cr.excute(select_xzqj_sql)
        xzqj = self._cr.fetchall()

        if not vals.get('bbrq'):
            vals['bbrq'] = datetime.datetime.utcnow()
        if login_user.glyh:
            vals['cjr'] = login_user.glyh.id 
            vals['gsmc'] = login_user.glyh.dqgs.id
            vals['bbqjn'] = xzqj[0][0]
            vals['bbqjy'] = xzqj[0][1]
            vals['zt'] = u'填写'
            vals['display_bbqj'] = xzqj[0][0] + "-"+xzqj[0][1]
            vals['bbbh'] = getbbbh('yszlb',self)
            vals['bbmc'] = u'名称'
            select_gsmc_sql = \
                """
                select name from gs where id = %s
                """%vals['gsmc']
            self._cr.excute(select_gsmc_sql)
            gsmc = self._cr.fetchall()

            vals['display_gsqj'] = gsmc[0][0] + " " + xzqj[0][1] + "-" + xzqj[0][1]

            #判断是否已存在
            cjgs = login_user.glyh.dqgs.id
            bbqjn = vals['bbqjn']
            bbqjy = vals['bbqjy']

            this_month_sql = \
                """
                select id from yszlb where bbqjn = '%s' and bbqjy = '%s' and gsmc = '%s'
                """%(bbqjn,bbqjy,cjgs)
            self._cr.excute(this_month_sql)
            count = self._cr.fetchall()
            if count:
                raise.UserError("当月  已存在")
            res = super(yszlb,self).create(vals)
            return res


    @api.multi
    def bat_second(self):
        if not check_permit(self,'yszlb','驳回'):
            raise.UserError('权限不足')
        fyb = self.browse(self._context.get('active_ids'))
        for hzb in fyb:
            if hzb.zt == u'填写':
                raise.UserError('已为填写状态')
            if not hzb.zt == u'接收':
                raise.UserError('状态不是接收')
            hzb.zt = u'填写'
            sql = \
                """
                update yszlsj set zt = '填写' where yszlsj = %s
                """%hzb.ids[0]
            self.excute(sql)
        return True

        

