# -*- coding: utf-8 -*-
import os
import time
import platform
import subprocess
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
from common.base import logger

import threading

class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)

class AppiumServer(object):
    def __init__(self,kwargs):
        self.kwargs=kwargs

    def run(self,url):
        time.sleep(10)
        response = urllib.request.urlopen(url, timeout=5)
        if str(response.getcode()).startswith("2"):
            return True

    def start_server(self):#开启服务
        for i in range(0, len(self.kwargs)):
            cmd = "appium  -p %s  " % (
                self.kwargs[i]["port"])
            if platform.system() == "Windows":  # windows下启动server
                t1 = RunServer(cmd)
                p = Process(target=t1.start())
                p.start()
                while True:
                    time.sleep(4)
                    if self.run("http://127.0.0.1:4723" + "/wd/hub/status"):
                        logger.info("-------win_server_successfully--------------")
                        break
            else:
                appium = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
                                          close_fds=True)

                while True:
                    appium_line = appium.stdout.readline().strip().decode()
                    time.sleep(2)
                    if 'listener started' in appium_line or 'Error: listen' in appium_line:
                        print("----server start successfully---")
                        break

    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()

    def stop_server(self,post_num=4723):
        sysstr = platform.system()
        if sysstr == 'Windows':
            p = os.popen(f'netstat  -aon|findstr {post_num}')
            p0 = p.read().strip()
            if p0 != '' and 'LISTENING' in p0:
                p1 = int(p0.split('LISTENING')[1].strip()[0:4])
                os.popen(f'taskkill /F /PID {p1}')
                print('appium server stopped')
        else:
            p = os.popen(f'lsof -i tcp:{post_num}')
            p0 = p.read()
            if p0.strip() != '':
                p1 = int(p0.split('\n')[1].split()[1])
                os.popen(f'kill {p1}')
                print('appium server stopped ')

    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        for i in range(0, len(self.kwargs)):
            url = " http://127.0.0.1:"+str(self.kwargs[i]["port"])+"/wd/hub"+"/status"
            try:
                response = urllib.request.urlopen(url, timeout=5)

                if str(response.getcode()).startswith("2"):
                    return True
                else:
                    return False
            except URLError:
                return False
            finally:
                if response:
                    response.close()

# if __name__ == "__main__":
#
#     oo = AppiumServer()
#     oo.start_server()
#     print("strart server")
#     print("running server")
#     oo.stop_server()
#     print("stop server")