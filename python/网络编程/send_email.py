# SMTP 服务
import smtplib
# 邮件头部
import email.mime.multipart
# 邮件内容
import email.mime.text

email_user = '1781082307@qq.com'
email_recv = 'szhu9903@gmail.com'
email_password = 'dkflesshnbzhbafc'
email_server = 'smtp.qq.com'

message = email.mime.multipart.MIMEMultipart()
message['from'] = email_user
message['to'] = email_recv
message['subject'] = '测试邮件处理'

content = """
int main()
{
    int i = 10;
    printf(' z朱num data %d \\n' % i);
    return 0;
}
"""
content_add = email.mime.text.MIMEText(content)
message.attach(content_add)

smtp = smtplib.SMTP_SSL(email_server, 456)
smtp.login(email_user, email_password)
recv_data = smtp.sendmail(email_user, email_recv, message.as_string())
smtp.close()


