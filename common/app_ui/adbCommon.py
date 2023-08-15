
import os
import subprocess
#you should prepare adb command
class AndroidDebugBridge(object):
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # check for any fastboot device
    def fastboot(self, device_id):
        pass

    # check devices
    # def attached_devices(self):
    #     result = self.call_adb("devices")
    #     devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
    #     flag = [device for device in devices if len(device) > 2]
    #     if flag:
    #         return True
    #     else:
    #         return False
    #         # return [device for device in devices if len(device) > 2]

    def attached_devices(self):
        devices = []
        result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).stdout.readlines()

        for item in result:
            t = item.decode().split("\tdevice")
            if len(t) >= 2:
                devices.append(t[0])
        return devices

    # get status
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None
    #reboot
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # copy file from PC to device
    def push(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # puu data to local
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s" % (remote, local))
        return result

    # sync command
    def sync(self, directory, **kwargs):
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = self.call_adb(command)
            return result

    # open app
    def open_app(self,packagename,activity):
        result = self.call_adb("shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # get pid according to package
    def get_app_pid(self, pkg_name):
        string = self.call_adb("shell ps | grep "+pkg_name)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        return result[4]

#test
# reuslt = AndroidDebugBridge().attached_devices()
# print(reuslt)
