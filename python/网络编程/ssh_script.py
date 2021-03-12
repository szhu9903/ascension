from python import logger
from tkinter import filedialog
import tkinter as tk
import paramiko
import time

class sshScript():
    # 初始参数
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.port = 22
        self.username = username
        self.password = password
        # 保存连接的ssh对象
        self.ssh = None
        self.res = None
        self.sftp = None

    # 建立连接
    def connect(self):
        try:
            self.ssh = paramiko.Transport(sock = (self.hostname, self.port))
            self.ssh.connect(username = self.username, password = self.password)
            self.sftp = paramiko.SFTPClient.from_transport(self.ssh)
            self.res = self.ssh.open_session()
            self.res.settimeout(30)
            self.res.get_pty()
            self.res.invoke_shell()
            logger.info('连接%s成功' % self.hostname)
            print(self.res.recv(65535).decode('utf-8'))
            return
        except Exception as Err:
            logger.error('失败%s' % Err)
            exit(1)

    # 发送命令行命令
    def send(self, cmd):
        cmd += '\r'
        result = ''
        self.res.send(cmd)
        # TODO 读取部分待修改
        while True:
            time.sleep(0.5)
            result += self.res.recv(65535).decode('utf-8')
            return result

    # 上传文件
    def up_file(self, up_file, up_path):
        try:
            result = self.sftp.put(up_file, up_path)
            return result
        except Exception as Err:
            logger.error('失败%s' % Err)
        self.close()

    # 关闭连接
    def close(self):
        self.sftp.close()
        self.res.close()
        self.ssh.close()


if __name__ == '__main__':
    file = ''
    def get_path():
        file = filedialog.askopenfilename()
        path.set(file)

    def send_file():
        try:
            # 获取地址
            file_path = path.get()
            ssh_path = res.get()
            # 连接
            ssh_conn = sshScript('47.**.**.**', 'ssh_user', '**********')
            ssh_conn.connect()
            # 上传
            up_result = ssh_conn.up_file(file_path, ssh_path)
            if up_result:
                res.set('SUCCESS')
        except Exception as Err:
            logger.error('失败%s' % Err)
        ssh_conn.close()


    root = tk.Tk()
    path = tk.StringVar()
    res = tk.StringVar()

    tk.Button(root, text = '选择路径', command = get_path).grid(row = 0, column = 0)
    tk.Entry(root, textvariable = path).grid(row = 0, column = 1)
    tk.Label(root, text='远程路径').grid(row=1, column=0)
    tk.Entry(root, textvariable = res).grid(row=1, column=1)
    tk.Button(root, text = '上传', command = send_file).grid(row = 2, column = 0)

    root.mainloop()

    # ssh_conn = sshScript('47.**.**.**', 'user', '**********')
    # ssh_conn.connect()
    # try:
    #     # 发送命令
    #     result = ssh_conn.send('docker images')
    #     print(result)
    #     # 上传文件, 本地文件路径，要上传到的位置
    #     up_result = ssh_conn.up_file(r"E:/channel_v3.json", '/home/up_test.json')
    #     if up_result:
    #         # 检验上传结果
    #         ssh_conn.send('cd /home')
    #         res_ls = ssh_conn.send('ll')
    #         print(res_ls)
    # except Exception as Err:
    #     logger.error('失败%s' % Err)
    # ssh_conn.close()
