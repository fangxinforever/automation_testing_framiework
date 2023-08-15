import pytest
import globals


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="chrome",
                     help="Choose the platform to run test cases! Support chrome, firefox, ie, edge, android, ios")
    parser.addoption("--env", action="store", default="QA", help="Testing environment")
    parser.addoption('--app', action='store', default="android", help="Choose App: ios or android")
    parser.addoption('--device', action='store', default="emulator", help="Choose Device: simulator / emulator / real "
                                                                          "device")

def pytest_configure(config):
    globals.set("platform", config.getoption("platform"))
    globals.set("env", config.getoption("env"))

@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")

@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")
