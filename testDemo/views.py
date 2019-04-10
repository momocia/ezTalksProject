# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render,redirect,HttpResponse,render_to_response,HttpResponseRedirect
from testDemo import models
import json
import urllib2
import paramiko
from time import sleep
import urllib2
import os
from django import forms
from testDemo.models import TUserinfo
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
import hashlib


# Create your views here.


def roominfo(request):
    if request.method == 'GET':
        return render(request,'Roominfo.html')
    elif request.method == 'POST':
        mid = request.POST.get('meetingid')
        roomlog_list = models.TRoomlog.objects.filter(roomid__in= models.TRoominfo.objects.filter(loginroomno=mid)).order_by('-entertime')
        print(roomlog_list)
        for i in roomlog_list:
            print(i.entertime)

        return render(request,'Roominfo.html',{'roomlog_list':roomlog_list})

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def upload_ajax(request):

    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        f = open(os.path.join(BASE_DIR, 'static', 'files', file_obj.name), 'wb')
        print('-------- 开始更新UC服务器  --------')
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        print('文件上传至缓存.')
        sleep(1)
        web_home = "/home/fsmeeting/eztalks_boss/install/"
        # 连接服务器120.26.132.173
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('120.26.132.173', 2201, 'fsmeeting', 'fsmeeting123')
        stdin, stdout, stderr = ssh.exec_command(
            'rm -rf /home/fsmeeting/eztalks_boss/install/*.zip')
        print "\n\033[0;31;0m*DELETING *.zip files  ...\033[0m"

        # 文件上传
        transport = paramiko.Transport(('120.26.132.173', 2201))
        transport.connect(username='fsmeeting', password='fsmeeting123')
        sftp = paramiko.SFTPClient.from_transport(transport)
        print "\n*Upload Start ..."
        sftp.put('D:/ezTalksProject/static/files/dist.zip', web_home + 'dist.zip')
        print "*Upload End ..."
        transport.close()
        # 文件备份
        stdin, stdout, stderr = ssh.exec_command(
            'rm -rf /home/fsmeeting/eztalks_boss/install/bak/newuc')
        sleep(1)
        stdin, stdout, stderr = ssh.exec_command(
            'mv /home/fsmeeting/eztalks_boss/install/newuc /home/fsmeeting/eztalks_boss/install/bak/')
        print "原版本已备份."

        # 文件解压
        sleep(2)

        stdin, stdout, stderr = ssh.exec_command(
            'unzip /home/fsmeeting/eztalks_boss/install/dist.zip -d /home/fsmeeting/eztalks_boss/install/newuc')
        sleep(1)
        msg='UC服务器已更新'
        return HttpResponse(json.dumps(msg,ensure_ascii=False))

def webinar_upload(request):

    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        f = open(os.path.join(BASE_DIR, 'static', 'files', file_obj.name), 'wb')
        print('-------- 开始更新Webinar服务器  --------')
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        print('文件上传至缓存')
        sleep(1)
        web_home = "/home/fsmeeting/eztalks_boss/install/"
        # 连接服务器120.26.132.173
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('120.26.132.173', 2201, 'fsmeeting', 'fsmeeting123')
        stdin, stdout, stderr = ssh.exec_command(
            'rm -rf /home/fsmeeting/eztalks_boss/install/*.zip')
        print "\n\033[0;31;0m*DELETING *.zip files  ...\033[0m"

        # 文件上传
        transport = paramiko.Transport(('120.26.132.173', 2201))
        transport.connect(username='fsmeeting', password='fsmeeting123')
        sftp = paramiko.SFTPClient.from_transport(transport)
        print "\n*Upload Start ..."
        sftp.put('D:/ezTalksProject/static/files/out.zip', web_home + 'out.zip')
        print "*Upload End ..."
        transport.close()
        # 文件备份
        stdin, stdout, stderr = ssh.exec_command(
            'rm -rf /home/fsmeeting/eztalks_boss/install/bak/webinar')
        sleep(1)
        stdin, stdout, stderr = ssh.exec_command(
            'mv /home/fsmeeting/eztalks_boss/install/webinar /home/fsmeeting/eztalks_boss/install/bak/')
        print "原版本已备份."

        # 文件解压
        sleep(2)

        stdin, stdout, stderr = ssh.exec_command(
            'unzip /home/fsmeeting/eztalks_boss/install/out.zip -d /home/fsmeeting/eztalks_boss/install/webinar')
        sleep(1)
        msg='Webinar服务器已更新'
        return HttpResponse(json.dumps(msg,ensure_ascii=False))



def server(request):
    if request.method == 'GET':
        return render(request, 'Server.html')
    elif  request.method == 'POST':
            JenID =request.POST.get('JenID')
            serverPWD = request.POST.get('serverPWD')
            msg ='Done'
            try:
                if int(serverPWD) == 147258:
                    print(JenID)
                    print "\033[0;34;0m\n-------- GET files from Jenkins--------\033[0m"
                    url_core = 'http://192.168.5.30:8088/jenkins/view/eztalks/job/build_ez_boss/' + JenID + '/artifact/ez-core/target/ez-core.war'
                    url_api = 'http://192.168.5.30:8088/jenkins/view/eztalks/job/build_ez_boss/' + JenID + '/artifact/ez-api/target/ez-api.war'
                    f_core = urllib2.urlopen(url_core)
                    f_api = urllib2.urlopen(url_api)
                    data_core = f_core.read()
                    data_api = f_api.read()
                    with open("E:/temp/ez-core.war", "wb") as code1:
                        code1.write(data_core)
                    print "\033[0;32;0m--- Downloading ez-core from \033[0m"+url_core
                    with open("E:/temp/ez-api.war", "wb") as code2:
                        code2.write(data_api)
                    print "\033[0;32;0m--- Downloading ez-api from \033[0m"+url_api

                    web_home = "/home/fsmeeting/eztalks_boss/install/"
                    # 连接服务器120.26.132.173
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect('120.26.132.173', 2201, 'fsmeeting', 'fsmeeting123')
                    stdin, stdout, stderr = ssh.exec_command(
                        'rm -rf /home/fsmeeting/eztalks_boss/install/*.war /home/fsmeeting/eztalks_boss/install/*.zip')
                    print "\n\033[0;31;0m-------- DELETING war/zip files  --------\033[0m"

                    # 文件上传
                    transport = paramiko.Transport(('120.26.132.173', 2201))
                    transport.connect(username='fsmeeting', password='fsmeeting123')
                    sftp = paramiko.SFTPClient.from_transport(transport)
                    print "\n-------- Upload Start...--------"
                    sftp.put('E:/temp/ez-core.war', web_home + 'ez-core.war')
                    sftp.put('E:/temp/ez-api.war', web_home + 'ez-api.war')
                    print "-------- Upload End     --------"
                    transport.close()

                    # 文件备份
                    stdin, stdout, stderr = ssh.exec_command(
                        'sh /home/fsmeeting/eztalks_boss/install/tomcat.sh stop')  # 关闭tomcat
                    print "\033[0;31;0m\n-------- Tomcat Closed  --------\033[0m"
                    sleep(1)
                    print "-------- Back-up Begin    --------"
                    stdin, stdout, stderr = ssh.exec_command(
                        'rm -rf /home/fsmeeting/eztalks_boss/install/bak/ez-core /home/fsmeeting/eztalks_boss/install/bak/ez-api')
                    sleep(1)
                    stdin, stdout, stderr = ssh.exec_command(
                        'mv /home/fsmeeting/eztalks_boss/install/ez-core /home/fsmeeting/eztalks_boss/install/bak/')
                    sleep(1)
                    stdin, stdout, stderr = ssh.exec_command(
                        'mv /home/fsmeeting/eztalks_boss/install/ez-api /home/fsmeeting/eztalks_boss/install/bak/')
                    print "-------- Back-up Finshed  --------"

                    # 文件解压
                    sleep(2)

                    stdin, stdout, stderr = ssh.exec_command(
                        'unzip /home/fsmeeting/eztalks_boss/install/ez-api.war -d /home/fsmeeting/eztalks_boss/install/ez-api')
                    sleep(5)
                    stdin, stdout, stderr = ssh.exec_command(
                        'unzip /home/fsmeeting/eztalks_boss/install/ez-core.war -d /home/fsmeeting/eztalks_boss/install/ez-core')
                    sleep(5)

                    print "-------- Unzip Done     --------\n"

                    # 启动tomcat
                    stdin, stdout, stderr = ssh.exec_command('sh /home/fsmeeting/eztalks_boss/install/tomcat.sh start')
                    log = stdout.read()
                    print "\033[0;34;0m-------- Tomcat Starting --------\n\033[0m"
                    print "\033[0;35;0m%s\033[0m" % log

                    sleep(1)
                    print "\033[0;34;0m-------- Tomcat Started --------\033[0m"
                    return HttpResponse(json.dumps(msg))
                else:
                    msg = '密码错误，中止操作'
                    return HttpResponse(json.dumps(msg))
            except ValueError as e:
                # msg =str(e)
                msg = '密码不能为空'
            except urllib2.URLError,e:
                # msg = str(e)
                msg = '密码验证已通过,无法识别Jenkins构建编号'
            return HttpResponse(json.dumps(msg))

# 登录
#定义表单类型
class UserLoginForm(forms.Form):
    username=forms.CharField(label='username',
                             max_length=100,
                             min_length=6,
                             error_messages={
                                 'required': '用户名不能为空',
                                 'max_length': '太长了',
                                 'min_length': '太短了',
                             },
                             )
    password=forms.CharField(label='password',widget=forms.PasswordInput())
#登录login
def login(request):
    if request.method =='GET':
        return render(request,'login.html')

    # elif request.method=='POST':
    #     print("post")
    #     uf=UserLoginForm(request.POST)
    #     print(uf)
    #     if uf.is_valid():
    #         #获取表单信息
    #         username=uf.cleaned_data['username']
    #         # password=uf.cleaned_data['password']
    #         password =  hashlib.md5(uf.cleaned_data['password']).hexdigest()
    #         print(username,password)
    #         #获得的表单和数据库比较
    #         try:
    #             user=TUserinfo.objects.get(username=username,password=password)
    #             print("数据库校验成功")
    #             return redirect('/server')
    #         except ObjectDoesNotExist:
    #             print(uf.errors)
    #             return HttpResponseRedirect('/login',{'uf':uf},{'uf':uf})
    #     else:
    #         return render(request,'login.html',{'uf':uf})
