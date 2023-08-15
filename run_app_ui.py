import pytest
import os
import time
import datetime
import unittest
from common.base.yml_util import read_yml
from common.base import dataToString
from common.app_ui import adbCommon
from common.app_ui import server
from common.app_ui.runnerBase import TestInterfaceCase
from multiprocessing import Pool
from common.base.path import Base_path
from common.app_ui.parmer import Parmer
from test_cases.app_ui.example.regtest import regtest
def get_appium_config():
    return read_yml("common/app_ui/devices.yaml")
def runnerCaseApp(devices):
    suite = unittest.TestSuite()
    suite.addTest(Parmer.parametrize(testcase_klass=regtest, parames=devices))
    unittest.TextTestRunner(verbosity=2).run(suite)
def runnerPool(device):
    devices_Pool = []
    # for i in range(0, len(device)):
    l_pool = []
    capability = {}
    capability["deviceType"] = device["deviceType"]
    capability["deviceName"] = device["deviceName"]
    capability["platformVersion"] = device["platformVersion"]
    capability["platformName"] = device["platformName"]
    capability["platformType"] = device["platformType"]
    capability["app"] = os.path.join(Base_path, device["app"])
    capability["port"] = device["port"]
    l_pool.append(capability)
    devices_Pool.append(l_pool)
    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()
def get_attach_devices():
    androidDebugBridge = adbCommon.AndroidDebugBridge()
    return androidDebugBridge.attached_devices()

def get_devices_list():
    androidDebugBridge = adbCommon.AndroidDebugBridge()
    return androidDebugBridge.call_adb("devices")

if __name__ == '__main__':
    # pytest.main(["-s", "-v", "test_cases/app_ui", "--alluredir=test_results/reports/app_ui/allure-results"])
    appium_config = get_appium_config()
    devices =get_attach_devices()
    if len(devices)!= 0:
        appium_server = server.AppiumServer(appium_config['appium'])
        appium_server.start_server()
        # while not appium_server.is_runnnig():
        #     time.sleep(2)
        runnerPool(appium_config['devices']['test_local'])
        appium_server.stop_server(appium_config['appium'][0]['port'])
