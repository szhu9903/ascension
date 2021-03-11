from python import logger

# SMTP 服务
import smtplib
from email.mime.text import MIMEText
from email.header import Header

email_user = '1781082307@qq.com'
email_recv = 'szhu9903@gmail.com'
email_code = 'dkflesshnbzhbafc'
email_server = 'smtp.qq.com'
email_port = 465

stmp = smtplib.SMTP_SSL(email_server, email_port)
stmp.login(email_user, email_code)
logger.info('服务器连接成功')

content = """
int main()
{
    int i = 10;
    printf(' z朱num data %d \\n' % i);
    return 0;
}
"""
# 拼装数据体
message = MIMEText(content, 'plain', 'utf-8')
# 发件人
message['From'] = Header('Python Smtp Szhu', 'utf-8')
# 收件人
message['To'] = Header('Szhu', 'utf-8')
# 标题
message['Subject'] = Header('Python Smtp 本地测试', 'utf-8')

try:
    stmp.sendmail(email_user, email_recv, message.as_string())
except Exception as err:
    logger.error('失败%s' % err)
logger.info('发送成功。')