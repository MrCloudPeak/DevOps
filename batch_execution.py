#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko


def run(host_ip, username, password, command):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host_ip, 22, username, password)
        print('===================exec on [%s]=====================' % host_ip)
        print(ssh.exec_command(command, timeout=300)[1].read())
    except Exception as ex:
        print('error, host is [%s], msg is [%s]' % (host_ip, ex.message))
    finally:
        ssh.close()


if __name__ == '__main__':
    # 将需要批量执行命令的host ip地址填到这里
    # eg: host_ip_list = ['192.168.1.2', '192.168.1.3']
    host_ip_list = ['ip1', 'ip2']
    for _host_ip in host_ip_list:
        # 用户名，密码，执行的命令填到这里
        # eg: run(_host_ip, 'root', 'root123', 'yum install -y redis')
        run(_host_ip, 'your_username', 'your_password', 'your command')
