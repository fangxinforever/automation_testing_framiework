
from common.app_ui import server
# control appium server
class AppiumServer():
    def __init__(self,devices):
        self.server = server.AppiumServer(devices)
    def start_server(self):
        self.server.start_server()
    def stop_server(self):
        self.server.stop_server()
    def is_runnnig(self):
        return self.server.is_runnnig()